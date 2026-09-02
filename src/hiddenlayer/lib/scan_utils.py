"""
Shared utilities for scan functionality across different scanner types.

This module provides common retry logic for handling scan retrieval operations
that may initially return 404 errors due to timing issues.

Scan reports are assembled from the summary endpoint plus the cursor-paginated
file-results endpoint; the unpaginated results endpoint is not used.
"""

import time
import random
import asyncio
import logging
from typing import TYPE_CHECKING, Any, Dict, List

from .._exceptions import NotFoundError
from ..types.scans import ScanReport

if TYPE_CHECKING:
    from .. import HiddenLayer, AsyncHiddenLayer

logger = logging.getLogger(__name__)


class ScanStatus:
    """Scan status constants."""

    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    CANCELED = "canceled"


# Page size and inter-page delay for collecting file results. The delay
# throttles reconstruction of massive scans (10k+ files) so the SDK never
# hammers the API with back-to-back page reads.
FILE_RESULTS_PAGE_SIZE = 100
FILE_RESULTS_PAGE_DELAY_SECONDS = 0.25

# Deprecated top-level report fields that mirror `.summary.*` per the API contract.
_DEPRECATED_SUMMARY_MIRROR_FIELDS = (
    "detection_count",
    "file_count",
    "files_with_detections_count",
    "detection_categories",
    "severity",
)


def _build_scan_report(summary: Any, file_results: List[Any]) -> "ScanReport":
    """Assemble a full ScanReport from a scan summary plus its paginated file results."""
    data: Dict[str, Any] = summary.model_dump()
    data["file_results"] = [file_result.model_dump() for file_result in file_results]
    nested_summary = data.get("summary") or {}
    for field in _DEPRECATED_SUMMARY_MIRROR_FIELDS:
        if field not in data and field in nested_summary:
            data[field] = nested_summary[field]
    return ScanReport.construct(**data)


def _collect_file_results(client: "HiddenLayer", *, scan_id: str) -> List[Any]:
    """Fetch every file result for a scan, throttling between page reads."""
    page = client.scans.results.list_files(scan_id, page_size=FILE_RESULTS_PAGE_SIZE)
    file_results: List[Any] = list(page.items or [])
    while page.has_next_page():
        time.sleep(FILE_RESULTS_PAGE_DELAY_SECONDS)
        page = page.get_next_page()
        file_results.extend(page.items or [])
    return file_results


async def _collect_file_results_async(client: "AsyncHiddenLayer", *, scan_id: str) -> List[Any]:
    """Async version of _collect_file_results."""
    page = await client.scans.results.list_files(scan_id, page_size=FILE_RESULTS_PAGE_SIZE)
    file_results: List[Any] = list(page.items or [])
    while page.has_next_page():
        await asyncio.sleep(FILE_RESULTS_PAGE_DELAY_SECONDS)
        page = await page.get_next_page()
        file_results.extend(page.items or [])
    return file_results


def get_scan_results(client: "HiddenLayer", *, scan_id: str) -> "ScanReport":
    """
    Get the scan report with retry logic for 404 errors.

    Used when wait_for_results=False to handle initial scan availability.

    The report is assembled from the summary endpoint plus the paginated
    file-results endpoint. If the scan is still running, the assembled report
    is a point-in-time snapshot: paginating over an active scan may miss or
    duplicate file entries.
    """
    retries = 0
    max_retries = 5  # Fewer retries since we're not waiting for completion
    base_delay = 0.5  # Slightly longer base delay

    while retries < max_retries:
        try:
            summary = client.scans.results.retrieve_summary(scan_id)
            file_results = _collect_file_results(client, scan_id=scan_id)
            return _build_scan_report(summary, file_results)
        except NotFoundError:
            retries += 1
            if retries >= max_retries:
                logger.error(f"Scan {scan_id} not found after {max_retries} attempts")
                raise

            delay = base_delay * retries + random.uniform(0, 0.5)
            logger.info(f"Scan not yet available, retrying in {delay:.1f}s (attempt {retries + 1}/{max_retries})")
            time.sleep(delay)

    # Should never reach here due to raise above, but satisfy linter
    raise RuntimeError(f"Scan {scan_id} not found after {max_retries} attempts")


def wait_for_scan_results(client: "HiddenLayer", *, scan_id: str) -> "ScanReport":
    """
    Wait for the scan to finish, then assemble the full report.

    Polls the lightweight summary endpoint for status; once the scan reaches a
    terminal state, the report is assembled from that summary plus the
    paginated file-results endpoint (throttled between pages).

    Handles initial 404 errors when scan is not immediately available.
    """
    base_delay = 0.1  # seconds
    retries = 0

    while True:
        try:
            summary = client.scans.results.retrieve_summary(scan_id)
            # If we got here, scan exists - check if it's done
            if summary.status in [ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED]:
                break
            logger.info(f"scan status: {summary.status}")
        except NotFoundError:
            # Scan not found yet, treat it like any other retry condition
            logger.info(f"scan not found yet, retrying...")

        retries += 1
        delay = base_delay * 2**retries + random.uniform(0, 1)  # exponential back off retry
        delay = min(delay, 30)  # cap at 30 seconds
        time.sleep(delay)

    file_results = _collect_file_results(client, scan_id=scan_id)
    return _build_scan_report(summary, file_results)


async def get_scan_results_async(client: "AsyncHiddenLayer", *, scan_id: str) -> "ScanReport":
    """
    Async version of get_scan_results.

    Used when wait_for_results=False to handle initial scan availability.
    """
    retries = 0
    max_retries = 5  # Fewer retries since we're not waiting for completion
    base_delay = 0.5  # Slightly longer base delay

    while retries < max_retries:
        try:
            summary = await client.scans.results.retrieve_summary(scan_id)
            file_results = await _collect_file_results_async(client, scan_id=scan_id)
            return _build_scan_report(summary, file_results)
        except NotFoundError:
            retries += 1
            if retries >= max_retries:
                logger.error(f"Scan {scan_id} not found after {max_retries} attempts")
                raise

            delay = base_delay * retries + random.uniform(0, 0.5)
            logger.info(f"Scan not yet available, retrying in {delay:.1f}s (attempt {retries + 1}/{max_retries})")
            await asyncio.sleep(delay)

    # Should never reach here due to raise above, but satisfy linter
    raise RuntimeError(f"Scan {scan_id} not found after {max_retries} attempts")


async def wait_for_scan_results_async(client: "AsyncHiddenLayer", *, scan_id: str) -> "ScanReport":
    """
    Async version of wait_for_scan_results.

    Handles initial 404 errors when scan is not immediately available.
    """
    base_delay = 0.1  # seconds
    retries = 0

    while True:
        try:
            summary = await client.scans.results.retrieve_summary(scan_id)
            # If we got here, scan exists - check if it's done
            if summary.status in [ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED]:
                break
            logger.info(f"scan status: {summary.status}")
        except NotFoundError:
            # Scan not found yet, treat it like any other retry condition
            logger.info(f"scan not found yet, retrying...")

        retries += 1
        delay = base_delay * 2**retries + random.uniform(0, 1)  # exponential back off retry
        delay = min(delay, 30)  # cap at 30 seconds
        await asyncio.sleep(delay)

    file_results = await _collect_file_results_async(client, scan_id=scan_id)
    return _build_scan_report(summary, file_results)


class ScanResultMixin:
    """Mixin providing scan_result functionality for sync scanners."""

    _client: "HiddenLayer"

    def scan_result(self, *, scan_id: str) -> "ScanReport":
        """Get the scan report for a given scan id."""
        return get_scan_results(self._client, scan_id=scan_id)


class AsyncScanResultMixin:
    """Mixin providing scan_result functionality for async scanners."""

    _client: "AsyncHiddenLayer"

    async def scan_result(self, *, scan_id: str) -> "ScanReport":
        """Get the scan report for a given scan id."""
        return await get_scan_results_async(self._client, scan_id=scan_id)
