"""
Model scanning functionality for Hidden Layer SDK.

This module provides the model scanning methods that were available in the old SDK,
including scan_file and scan_folder methods with multipart upload functionality.
"""

import os
import time
import random
import logging
from typing import List, Union, Literal, Optional, Generator, cast
from fnmatch import fnmatch
from pathlib import Path
from typing_extensions import TYPE_CHECKING

import httpx

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from .. import HiddenLayer, AsyncHiddenLayer
    from ..types.scans import ScanReport

# Exclude patterns matching the old SDK
EXCLUDE_FILE_TYPES = [
    "*.txt",
    "*.md",
    "*.lock",
    ".gitattributes",
    ".git",
    ".git/*",
    "*/.git",
    "**/.git/**",
]

PathInputType = Union[str, os.PathLike[str]]


def filter_path_objects(
    items: Union[List[PathInputType], Generator[PathInputType, None, None]],
    *,
    allow_patterns: Optional[Union[List[str], str]] = None,
    ignore_patterns: Optional[Union[List[str], str]] = None,
) -> Generator[Union[str, os.PathLike[str]], None, None]:
    """Filter path objects based on an allowlist and a denylist.

    Input must be a list of paths (`str` or `Path`) or a generator of paths.

    Patterns are Unix shell-style wildcards which are NOT regular expressions. See
    https://docs.python.org/3/library/fnmatch.html for more details.

    :param items: List of paths to filter.
    :param allow_patterns: Patterns constituting the allowlist. If provided, item paths must match at
            least one pattern from the allowlist.
    :param ignore_patterns: Patterns constituting the denylist. If provided, item paths must not match
            any patterns from the denylist.

    :returns: Filtered list of objects, as a generator.
    """
    if isinstance(allow_patterns, str):
        allow_patterns = [allow_patterns]

    if isinstance(ignore_patterns, str):
        ignore_patterns = [ignore_patterns]

    def _identity(item: Union[str, os.PathLike[str]]) -> Path:
        if isinstance(item, str):
            return Path(item)
        if isinstance(item, Path):
            return item
        raise ValueError("Objects must be string or Pathlike.")

    key = _identity  # Items must be `str` or `Path`, otherwise raise ValueError

    for item in items:
        path: Path = key(item)

        if path.is_dir():
            continue

        # Skip if there's an allowlist and path doesn't match any
        if allow_patterns is not None and not any(fnmatch(str(path), r) for r in allow_patterns):
            continue

        # Skip if there's a denylist and path matches any
        if ignore_patterns is not None and any(fnmatch(str(path), r) for r in ignore_patterns):
            continue

        yield item


class ScanStatus:
    """Scan status constants matching the old SDK."""

    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    CANCELED = "canceled"


class ModelScanner:
    """
    Model scanner that provides file and folder scanning functionality.

    This class extends the generated SDK to provide the same functionality as the old SDK's
    ModelScanAPI, including multipart upload functionality for files and folders.
    """

    def __init__(self, client: "HiddenLayer") -> None:
        self._client = client

    def scan_file(
        self,
        *,
        model_name: str,
        model_path: Union[str, os.PathLike[str]],
        model_version: str = "1",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> "ScanReport":
        """
        Scan a local model file using the HiddenLayer Model Scanner.

        :param model_name: Name of the model to be shown on the HiddenLayer UI
        :param model_path: Local path to the model file.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param request_source: Source that requested the scan.
        :param origin: Origin platform where the model came from.

        :returns: Scan Results
        """
        file_path = Path(model_path)

        # Start the upload
        upload_response = self._client.scans.upload.start(
            model_name=model_name,
            model_version=model_version,
            requesting_entity="hiddenlayer-python-sdk",
            request_source=cast("Literal['Hybrid Upload', 'API Upload', 'Integration', 'UI Upload']", request_source),
            origin=origin,
        )

        scan_id = upload_response.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        # Upload the file
        self._scan_file(scan_id=scan_id, file_path=file_path)

        # Complete the upload
        self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = self._wait_for_scan_results(scan_id=scan_id)
        else:
            scan_results = self._client.scans.jobs.retrieve(scan_id)

        return scan_results

    def scan_folder(
        self,
        *,
        model_name: str,
        path: Union[str, os.PathLike[str]],
        model_version: str = "1",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> "ScanReport":
        """
        Submits all files in a directory and its sub directories to be scanned.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param path: Path to the folder on disk to be scanned.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param allow_file_patterns: If provided, only files matching at least one pattern are scanned.
        :param ignore_file_patterns: If provided, files matching any of the patterns are not scanned.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param request_source: Source that requested the scan.
        :param origin: Origin platform where the model came from.

        :returns: Scan Results
        """
        model_path = Path(path)

        # Start the upload
        upload_response = self._client.scans.upload.start(
            model_name=model_name,
            model_version=model_version,
            requesting_entity="hiddenlayer-python-sdk",
            request_source=cast("Literal['Hybrid Upload', 'API Upload', 'Integration', 'UI Upload']", request_source),
            origin=origin,
        )

        scan_id = upload_response.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        # Prepare file patterns
        ignore_file_patterns = EXCLUDE_FILE_TYPES + ignore_file_patterns if ignore_file_patterns else EXCLUDE_FILE_TYPES

        # Filter files
        files = filter_path_objects(
            model_path.rglob("*"),
            allow_patterns=allow_file_patterns,
            ignore_patterns=ignore_file_patterns,
        )

        # Upload each file
        for file in files:
            self._scan_file(scan_id=scan_id, file_path=Path(file))

        # Complete the upload
        self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = self._wait_for_scan_results(scan_id=scan_id)
        else:
            scan_results = self._client.scans.jobs.retrieve(scan_id)

        return scan_results

    def _scan_file(self, *, scan_id: str, file_path: Path) -> None:
        """Upload a single file using multipart upload."""
        filesize = file_path.stat().st_size

        # Initiate multipart upload for this file
        upload = self._client.scans.upload.file.add(
            scan_id=scan_id, file_name=str(file_path), file_content_length=filesize
        )

        # Upload each part
        with open(file_path, "rb") as f:
            for part in upload.parts:
                if part.start_offset is None:
                    raise Exception("part must have a start_offset")

                if part.end_offset is not None:
                    read_amount = part.end_offset - part.start_offset
                else:
                    read_amount = None

                f.seek(part.start_offset)
                part_data = f.read(read_amount)

                # Upload this part directly to the presigned URL
                if part.upload_url is None:
                    raise Exception("part.upload_url must not be None")

                response = httpx.put(
                    part.upload_url,
                    content=part_data,
                    headers={"Content-Type": "application/octet-stream"},
                )
                response.raise_for_status()

        # Complete the file upload
        self._client.scans.upload.file.complete(file_id=upload.upload_id, scan_id=scan_id)

    def _wait_for_scan_results(self, *, scan_id: str) -> "ScanReport":
        """
        Wait for scan results using exponential backoff polling.

        This mimics the behavior of the old SDK's _wait_for_scan_results method.
        """
        scan_results = self._client.scans.jobs.retrieve(scan_id)

        base_delay = 0.1  # seconds
        retries = 0
        logger.info(f"scan status: {scan_results.status}")

        while scan_results.status not in [ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED]:
            retries += 1
            delay = base_delay * 2**retries + random.uniform(0, 1)  # exponential back off retry
            delay = min(delay, 30)  # cap at 30 seconds
            time.sleep(delay)
            scan_results = self._client.scans.jobs.retrieve(scan_id)
            logger.info(f"scan status: {scan_results.status}")

        return scan_results


class AsyncModelScanner:
    """
    Async version of ModelScanner for use with AsyncHiddenLayer client.
    """

    def __init__(self, client: "AsyncHiddenLayer") -> None:
        self._client = client

    async def scan_file(
        self,
        *,
        model_name: str,
        model_path: Union[str, os.PathLike[str]],
        model_version: str = "1",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> "ScanReport":
        """
        Async version of scan_file.

        See ModelScanner.scan_file for parameter documentation.
        """
        file_path = Path(model_path)

        # Start the upload
        upload_response = await self._client.scans.upload.start(
            model_name=model_name,
            model_version=model_version,
            requesting_entity="hiddenlayer-python-sdk",
            request_source=cast("Literal['Hybrid Upload', 'API Upload', 'Integration', 'UI Upload']", request_source),
            origin=origin,
        )

        scan_id = upload_response.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        # Upload the file
        await self._scan_file(scan_id=scan_id, file_path=file_path)

        # Complete the upload
        await self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = await self._wait_for_scan_results(scan_id=scan_id)
        else:
            scan_results = await self._client.scans.jobs.retrieve(scan_id)

        return scan_results

    async def scan_folder(
        self,
        *,
        model_name: str,
        path: Union[str, os.PathLike[str]],
        model_version: str = "1",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> "ScanReport":
        """
        Async version of scan_folder.

        See ModelScanner.scan_folder for parameter documentation.
        """
        model_path = Path(path)

        # Start the upload
        upload_response = await self._client.scans.upload.start(
            model_name=model_name,
            model_version=model_version,
            requesting_entity="hiddenlayer-python-sdk",
            request_source=cast("Literal['Hybrid Upload', 'API Upload', 'Integration', 'UI Upload']", request_source),
            origin=origin,
        )

        scan_id = upload_response.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        # Prepare file patterns
        ignore_file_patterns = EXCLUDE_FILE_TYPES + ignore_file_patterns if ignore_file_patterns else EXCLUDE_FILE_TYPES

        # Filter files
        files = filter_path_objects(
            model_path.rglob("*"),
            allow_patterns=allow_file_patterns,
            ignore_patterns=ignore_file_patterns,
        )

        # Upload each file
        for file in files:
            await self._scan_file(scan_id=scan_id, file_path=Path(file))

        # Complete the upload
        await self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = await self._wait_for_scan_results(scan_id=scan_id)
        else:
            scan_results = await self._client.scans.jobs.retrieve(scan_id)

        return scan_results

    async def _scan_file(self, *, scan_id: str, file_path: Path) -> None:
        """Async version of _scan_file."""
        filesize = file_path.stat().st_size

        # Initiate multipart upload for this file
        upload = await self._client.scans.upload.file.add(
            scan_id=scan_id, file_name=str(file_path), file_content_length=filesize
        )

        # Upload each part
        with open(file_path, "rb") as f:
            for part in upload.parts:
                if part.start_offset is None:
                    raise Exception("part must have a start_offset")

                if part.end_offset is not None:
                    read_amount = part.end_offset - part.start_offset
                else:
                    read_amount = None

                f.seek(part.start_offset)
                part_data = f.read(read_amount)

                # Upload this part directly to the presigned URL
                if part.upload_url is None:
                    raise Exception("part.upload_url must not be None")

                async with httpx.AsyncClient() as client:
                    response = await client.put(
                        part.upload_url,
                        content=part_data,
                        headers={"Content-Type": "application/octet-stream"},
                    )
                    response.raise_for_status()

        # Complete the file upload
        await self._client.scans.upload.file.complete(file_id=upload.upload_id, scan_id=scan_id)

    async def _wait_for_scan_results(self, *, scan_id: str) -> "ScanReport":
        """
        Async version of _wait_for_scan_results.
        """
        import asyncio

        scan_results = await self._client.scans.jobs.retrieve(scan_id)

        base_delay = 0.1  # seconds
        retries = 0
        logger.info(f"scan status: {scan_results.status}")

        while scan_results.status not in [ScanStatus.DONE, ScanStatus.FAILED, ScanStatus.CANCELED]:
            retries += 1
            delay = base_delay * 2**retries + random.uniform(0, 1)  # exponential back off retry
            delay = min(delay, 30)  # cap at 30 seconds
            await asyncio.sleep(delay)
            scan_results = await self._client.scans.jobs.retrieve(scan_id)
            logger.info(f"scan status: {scan_results.status}")

        return scan_results
