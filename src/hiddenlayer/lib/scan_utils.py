"""Scan report retrieval shared by the model and community scanners.

A report is assembled from the summary endpoint and the cursor-paginated file-results endpoint.
A new scan can answer 404 for a moment, so both readers retry that.
"""

from __future__ import annotations

import asyncio
import logging
import random
import time
from typing import TYPE_CHECKING, Any, Dict, List

import httpx
from ..errors.not_found_error import NotFoundError
from ..types.scan_file_result_with_compliance_v3 import ScanFileResultWithComplianceV3
from ..types.scan_report_of_record_v3 import ScanReportOfRecordV3
from ..types.scan_report_summary_response_v3 import ScanReportSummaryResponseV3

if TYPE_CHECKING:
    from ..client import AsyncHiddenLayer, HiddenLayer

logger = logging.getLogger(__name__)

ScanReport = ScanReportOfRecordV3


class ScanStatus:
    """Scan status constants."""

    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    CANCELED = "canceled"


_TERMINAL_STATUSES = (ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED)

# The delay keeps a scan of 10k+ files from reading its pages back to back.
FILE_RESULTS_PAGE_SIZE = 100
FILE_RESULTS_PAGE_DELAY_SECONDS = 0.25

_NOT_FOUND_MAX_ATTEMPTS = 5
_NOT_FOUND_BASE_DELAY_SECONDS = 0.5
_POLL_BASE_DELAY_SECONDS = 0.1
_POLL_MAX_DELAY_SECONDS = 30
# Past this the delay is at its cap, and an unbounded exponent overflows a float after about 1,000 polls.
_POLL_MAX_EXPONENT = 10
# The generated client retries a failed connection, not a timeout or a dropped read as 3.x did.
_POLL_MAX_TRANSPORT_FAILURES = 3

# Deprecated top-level report fields that mirror `.summary.*` per the API contract.
_DEPRECATED_SUMMARY_MIRROR_FIELDS = (
    "detection_count",
    "file_count",
    "files_with_detections_count",
    "detection_categories",
    "severity",
)


def _build_scan_report(
    summary: ScanReportSummaryResponseV3, file_results: List[ScanFileResultWithComplianceV3]
) -> ScanReport:
    """Assembles a full report from a scan summary and its file results."""
    # A shallow copy of the fields, so nested models stay models: construct() does not validate.
    values: Dict[str, Any] = dict(summary)
    values["file_results"] = file_results
    for field in _DEPRECATED_SUMMARY_MIRROR_FIELDS:
        if values.get(field) is None:
            values[field] = getattr(summary.summary, field, None)
    return ScanReport.construct(**values)


def _not_found_delay(attempt: int) -> float:
    return _NOT_FOUND_BASE_DELAY_SECONDS * attempt + random.uniform(0, 0.5)


def _poll_delay(attempt: int) -> float:
    backoff = _POLL_BASE_DELAY_SECONDS * 2 ** min(attempt, _POLL_MAX_EXPONENT)
    return min(backoff + random.uniform(0, 1), _POLL_MAX_DELAY_SECONDS)


def _may_poll_again(error: httpx.TransportError, failures: int) -> bool:
    """Whether a status poll that failed in transit is retried: all but the third failure in a row."""
    if failures >= _POLL_MAX_TRANSPORT_FAILURES:
        return False
    logger.warning("scan status request failed, retrying: %r", error)
    return True


def _collect_file_results(client: "HiddenLayer", *, scan_id: str) -> List[ScanFileResultWithComplianceV3]:
    """Fetches every file result for a scan, pausing between pages."""
    file_results: List[ScanFileResultWithComplianceV3] = []
    for page in client.scans.results.list_files(scan_id, page_size=FILE_RESULTS_PAGE_SIZE).iter_pages():
        file_results.extend(page.items or [])
        if page.has_next:
            time.sleep(FILE_RESULTS_PAGE_DELAY_SECONDS)
    return file_results


async def _collect_file_results_async(
    client: "AsyncHiddenLayer", *, scan_id: str
) -> List[ScanFileResultWithComplianceV3]:
    file_results: List[ScanFileResultWithComplianceV3] = []
    pager = await client.scans.results.list_files(scan_id, page_size=FILE_RESULTS_PAGE_SIZE)
    async for page in pager.iter_pages():
        file_results.extend(page.items or [])
        if page.has_next:
            await asyncio.sleep(FILE_RESULTS_PAGE_DELAY_SECONDS)
    return file_results


def get_scan_results(client: "HiddenLayer", *, scan_id: str) -> ScanReport:
    """Returns the scan's report as it stands, without waiting for the scan to finish.

    For a scan that is still running the report is a snapshot: paging over an active scan can miss or
    repeat file results.

    Raises:
        NotFoundError: If the scan still isn't found after 5 attempts.
    """
    attempt = 0
    while True:
        try:
            summary = client.scans.results.retrieve_summary(scan_id)
            return _build_scan_report(summary, _collect_file_results(client, scan_id=scan_id))
        except NotFoundError:
            attempt += 1
            if attempt >= _NOT_FOUND_MAX_ATTEMPTS:
                logger.error("Scan %s not found after %d attempts", scan_id, _NOT_FOUND_MAX_ATTEMPTS)
                raise
            delay = _not_found_delay(attempt)
            logger.info(
                "Scan not yet available, retrying in %.1fs (attempt %d/%d)",
                delay,
                attempt + 1,
                _NOT_FOUND_MAX_ATTEMPTS,
            )
            time.sleep(delay)


def wait_for_scan_results(client: "HiddenLayer", *, scan_id: str) -> ScanReport:
    """Waits for the scan to finish, failed and canceled scans included, then returns its report.

    Polls the summary endpoint with exponential backoff, capped at 30 seconds, for as long as the scan runs.

    Raises:
        httpx.TransportError: If three status polls in a row time out or lose their connection.
    """
    attempt = 0
    transport_failures = 0
    while True:
        try:
            summary = client.scans.results.retrieve_summary(scan_id)
            transport_failures = 0
            if summary.status in _TERMINAL_STATUSES:
                break
            logger.info("scan status: %s", summary.status)
        except NotFoundError:
            logger.info("scan not found yet, retrying...")
        except httpx.TransportError as error:
            transport_failures += 1
            if not _may_poll_again(error, transport_failures):
                raise
        attempt += 1
        time.sleep(_poll_delay(attempt))
    return _build_scan_report(summary, _collect_file_results(client, scan_id=scan_id))


async def get_scan_results_async(client: "AsyncHiddenLayer", *, scan_id: str) -> ScanReport:
    """Async version of get_scan_results."""
    attempt = 0
    while True:
        try:
            summary = await client.scans.results.retrieve_summary(scan_id)
            return _build_scan_report(summary, await _collect_file_results_async(client, scan_id=scan_id))
        except NotFoundError:
            attempt += 1
            if attempt >= _NOT_FOUND_MAX_ATTEMPTS:
                logger.error("Scan %s not found after %d attempts", scan_id, _NOT_FOUND_MAX_ATTEMPTS)
                raise
            delay = _not_found_delay(attempt)
            logger.info(
                "Scan not yet available, retrying in %.1fs (attempt %d/%d)",
                delay,
                attempt + 1,
                _NOT_FOUND_MAX_ATTEMPTS,
            )
            await asyncio.sleep(delay)


async def wait_for_scan_results_async(client: "AsyncHiddenLayer", *, scan_id: str) -> ScanReport:
    """Async version of wait_for_scan_results."""
    attempt = 0
    transport_failures = 0
    while True:
        try:
            summary = await client.scans.results.retrieve_summary(scan_id)
            transport_failures = 0
            if summary.status in _TERMINAL_STATUSES:
                break
            logger.info("scan status: %s", summary.status)
        except NotFoundError:
            logger.info("scan not found yet, retrying...")
        except httpx.TransportError as error:
            transport_failures += 1
            if not _may_poll_again(error, transport_failures):
                raise
        attempt += 1
        await asyncio.sleep(_poll_delay(attempt))
    return _build_scan_report(summary, await _collect_file_results_async(client, scan_id=scan_id))


class ScanResultMixin:
    """Adds scan_result to the sync scanners."""

    _client: "HiddenLayer"

    def scan_result(self, *, scan_id: str) -> ScanReport:
        """Returns the scan's report as it stands; see get_scan_results."""
        return get_scan_results(self._client, scan_id=scan_id)


class AsyncScanResultMixin:
    """Adds scan_result to the async scanners."""

    _client: "AsyncHiddenLayer"

    async def scan_result(self, *, scan_id: str) -> ScanReport:
        """Returns the scan's report as it stands; see get_scan_results."""
        return await get_scan_results_async(self._client, scan_id=scan_id)
