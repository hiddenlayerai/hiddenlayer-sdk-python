"""
Shared utilities for scan functionality across different scanner types.

This module provides common retry logic for handling scan retrieval operations
that may initially return 404 errors due to timing issues.
"""

import time
import random
import asyncio
import logging
from typing import TYPE_CHECKING

from .._exceptions import NotFoundError

if TYPE_CHECKING:
    from .. import HiddenLayer, AsyncHiddenLayer
    from ..types.scans import ScanReport

logger = logging.getLogger(__name__)


class ScanStatus:
    """Scan status constants."""

    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    CANCELED = "canceled"


def get_scan_results(client: "HiddenLayer", *, scan_id: str) -> "ScanReport":
    """
    Get scan results with retry logic for 404 errors.

    Used when wait_for_results=False to handle initial scan availability.
    """
    retries = 0
    max_retries = 5  # Fewer retries since we're not waiting for completion
    base_delay = 0.5  # Slightly longer base delay

    while retries < max_retries:
        try:
            return client.scans.jobs.retrieve(scan_id)
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
    Wait for scan results using exponential backoff polling.

    Handles initial 404 errors when scan is not immediately available.
    """
    base_delay = 0.1  # seconds
    retries = 0
    scan_results = None

    while True:
        try:
            scan_results = client.scans.jobs.retrieve(scan_id)
            # If we got here, scan exists - check if it's done
            if scan_results.status in [ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED]:
                break
            logger.info(f"scan status: {scan_results.status}")
        except NotFoundError:
            # Scan not found yet, treat it like any other retry condition
            logger.info(f"scan not found yet, retrying...")

        retries += 1
        delay = base_delay * 2**retries + random.uniform(0, 1)  # exponential back off retry
        delay = min(delay, 30)  # cap at 30 seconds
        time.sleep(delay)

    return scan_results


async def get_scan_results_async(client: "AsyncHiddenLayer", *, scan_id: str) -> "ScanReport":
    """
    Async version of get_scan_results with retry logic for 404 errors.

    Used when wait_for_results=False to handle initial scan availability.
    """
    retries = 0
    max_retries = 5  # Fewer retries since we're not waiting for completion
    base_delay = 0.5  # Slightly longer base delay

    while retries < max_retries:
        try:
            return await client.scans.jobs.retrieve(scan_id)
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
    scan_results = None

    while True:
        try:
            scan_results = await client.scans.jobs.retrieve(scan_id)
            # If we got here, scan exists - check if it's done
            if scan_results.status in [ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED]:
                break
            logger.info(f"scan status: {scan_results.status}")
        except NotFoundError:
            # Scan not found yet, treat it like any other retry condition
            logger.info(f"scan not found yet, retrying...")

        retries += 1
        delay = base_delay * 2**retries + random.uniform(0, 1)  # exponential back off retry
        delay = min(delay, 30)  # cap at 30 seconds
        await asyncio.sleep(delay)

    return scan_results
