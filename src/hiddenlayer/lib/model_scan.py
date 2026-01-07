"""
Model scanning functionality for Hidden Layer SDK.

This module provides the model scanning methods that were available in the old SDK,
including scan_file and scan_folder methods with multipart upload functionality.
"""

import os
import logging
from typing import Any, Set, Dict, List, Union, Literal, Optional, Generator, cast
from fnmatch import fnmatch
from pathlib import Path
from typing_extensions import TYPE_CHECKING

from .scan_utils import get_scan_results, wait_for_scan_results, get_scan_results_async, wait_for_scan_results_async
from .._exceptions import BadRequestError

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


def is_duplicate_file_error(exc: BadRequestError) -> bool:
    """Check if a BadRequestError is due to duplicate files being detected."""
    body: object = exc.body
    if not isinstance(body, dict):
        return False
    detail = cast(Dict[str, Any], body).get("detail", "")
    return isinstance(detail, str) and "duplicate" in detail.lower()


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

    # Track resolved canonical paths to detect duplicates (handles symlinks and path normalization)
    seen: Set[str] = set()

    key = _identity  # Items must be `str` or `Path`, otherwise raise ValueError

    for item in items:
        path: Path = key(item)

        if path.is_dir():
            continue

        # Resolve to canonical path (follows symlinks, normalizes . and ..)
        try:
            resolved = str(path.resolve())
        except OSError:
            # Skip broken symlinks or files we can't access
            logger.debug("Skipping inaccessible path: %s", path)
            continue

        if resolved in seen:
            logger.debug("Skipping duplicate file (same resolved path): %s", path)
            continue

        seen.add(resolved)

        # Skip if there's an allowlist and path doesn't match any
        if allow_patterns is not None and not any(fnmatch(str(path), r) for r in allow_patterns):
            continue

        # Skip if there's a denylist and path matches any
        if ignore_patterns is not None and any(fnmatch(str(path), r) for r in ignore_patterns):
            continue

        yield item

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

        # Upload the file
        self._scan_file(scan_id=scan_id, file_path=file_path)

        # Complete the upload
        self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = wait_for_scan_results(self._client, scan_id=scan_id)
        else:
            scan_results = get_scan_results(self._client, scan_id=scan_id)

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
            try:
                self._scan_file(scan_id=scan_id, file_path=Path(file))
            except BadRequestError as e:
                if is_duplicate_file_error(e):
                    logger.warning("Duplicate file detected during folder scan, skipping: %s", file)
                    continue
                raise

        # Complete the upload
        self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = wait_for_scan_results(self._client, scan_id=scan_id)
        else:
            scan_results = get_scan_results(self._client, scan_id=scan_id)

        return scan_results

    def scan_s3_model(
        self,
        *,
        model_name: str,
        bucket: str,
        key: str,
        model_version: str = "1",
        s3_client: Optional[object] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> "ScanReport":
        """
        Scan a model file on S3.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param bucket: Name of the s3 bucket where the model file is stored.
        :param key: Path to the model file on s3.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param s3_client: boto3 s3 client.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param request_source: Source that requested the scan.

        :returns: Scan Results

        :examples:
            .. code-block:: python

                hl_client.model_scanner.scan_s3_model(
                    model_name="your-model-name", bucket="s3_bucket", key="path/to/file"
                )
        """
        try:
            import boto3  # type: ignore
        except ImportError as err:
            raise ImportError("Python package boto3 is not installed.") from err

        if not s3_client:
            s3_client = boto3.client("s3")  # type: ignore

        file_name = key.split("/")[-1]

        try:
            s3_client.download_file(bucket, key, f"/tmp/{file_name}")  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Couldn't download model s3://{bucket}/{key}: {e}") from e

        return self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            model_version=model_version,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="S3",
        )

    def scan_azure_blob_model(
        self,
        *,
        model_name: str,
        account_url: str,
        container: str,
        blob: str,
        model_version: str = "1",
        blob_service_client: Optional[object] = None,
        credential: Optional[object] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> "ScanReport":
        """
        Scan a model file on Azure Blob Storage.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param account_url: Azure Blob url of where the file is stored.
        :param container: Azure Blob container containing the model file.
        :param blob: Path to the model file inside the Azure blob container.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param blob_service_client: BlobServiceClient object. Defaults to creating one using DefaultCredential().
        :param credential: Credential to be passed to the BlobServiceClient object, can be a credential object, SAS key, etc.
            Defaults to `DefaultCredential`
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param request_source: Source that requested the scan.

        :returns: Scan Results

        :examples:
            .. code-block:: python

                hl_client.model_scanner.scan_azure_blob_model(
                    model_name="your-model-name",
                    account_url="https://<storageaccountname>.blob.core.windows.net",
                    container="container_name",
                    blob="path/to/file.bin",
                    credential="?<sas_key>",  # If using a SAS key and not DefaultCredentials
                )
        """
        try:
            from azure.identity import DefaultAzureCredential  # type: ignore
        except ImportError as err:
            raise ImportError("Python package azure-identity is not installed.") from err

        try:
            from azure.storage.blob import BlobServiceClient  # type: ignore
        except ImportError as err:
            raise ImportError("Python package azure-storage-blob is not installed.") from err

        if not credential:
            credential = DefaultAzureCredential()  # type: ignore

        if not blob_service_client:
            blob_service_client = BlobServiceClient(account_url, credential=credential)  # type: ignore

        file_name = blob.split("/")[-1]

        blob_client = blob_service_client.get_blob_client(  # type: ignore
            container=container, blob=blob
        )

        try:
            with open(os.path.join("/tmp", file_name), "wb") as f:
                download_stream = blob_client.download_blob()  # type: ignore
                f.write(download_stream.readall())  # type: ignore

        except Exception as e:
            raise RuntimeError(f"Couldn't download model {account_url}, {container}, {blob}: {e}") from e

        return self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            model_version=model_version,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="Azure Blob Storage",
        )

    def scan_huggingface_model(
        self,
        *,
        repo_id: str,
        model_name: Optional[str] = None,
        revision: Optional[str] = None,
        local_dir: str = "/tmp",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        force_download: bool = False,
        hf_token: Optional[Union[str, bool]] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> "ScanReport":
        """
        Scans a model on HuggingFace.

        Note: Requires the `huggingface_hub` pip package to be installed.

        :param repo_id: The HuggingFace repository id.
        :param model_name: Name of the model to be shown on the HiddenLayer UI. If not provided, uses repo_id.
        :param revision: An optional Git revision id which can be a branch name, a tag, or a commit hash.
        :param local_dir: If provided, the downloaded files will be placed under this directory.
        :param allow_file_patterns: If provided, only files matching at least one pattern are scanned.
        :param ignore_file_patterns: If provided, files matching any of the patterns are not scanned.
        :param force_download: Whether the file should be downloaded even if it already exists in the local cache.
        :param hf_token: A token to be used for the download.
            If True, the token is read from the HuggingFace config folder.
            If a string, it's used as the authentication token.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param request_source: Source that requested the scan.

        :returns: Scan Results
        """
        try:
            from huggingface_hub import snapshot_download  # type: ignore
        except ImportError as err:
            raise ImportError("Python package huggingface_hub is not installed.") from err

        local_dir = f"/tmp/{repo_id}" if local_dir == "/tmp" else local_dir
        ignore_file_patterns = EXCLUDE_FILE_TYPES + ignore_file_patterns if ignore_file_patterns else EXCLUDE_FILE_TYPES

        snapshot_download(
            repo_id,
            revision=revision,
            allow_patterns=allow_file_patterns,
            ignore_patterns=ignore_file_patterns,
            local_dir=local_dir,
            local_dir_use_symlinks=False,
            cache_dir=local_dir,
            force_download=force_download,
            token=hf_token,
        )

        if revision is None:
            revision = "1"

        return self.scan_folder(
            model_name=model_name or repo_id,
            model_version=revision,
            path=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="Hugging Face",
        )

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

                response = self._client._client.put(
                    part.upload_url,
                    content=part_data,
                    headers={"Content-Type": "application/octet-stream"},
                    timeout=self._client.timeout,
                )
                response.raise_for_status()

        # Complete the file upload
        self._client.scans.upload.file.complete(file_id=upload.upload_id, scan_id=scan_id)


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

        # Upload the file
        await self._scan_file(scan_id=scan_id, file_path=file_path)

        # Complete the upload
        await self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = await wait_for_scan_results_async(self._client, scan_id=scan_id)
        else:
            scan_results = await get_scan_results_async(self._client, scan_id=scan_id)

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
            try:
                await self._scan_file(scan_id=scan_id, file_path=Path(file))
            except BadRequestError as e:
                if is_duplicate_file_error(e):
                    logger.warning("Duplicate file detected during folder scan, skipping: %s", file)
                    continue
                raise

        # Complete the upload
        await self._client.scans.upload.complete_all(scan_id=scan_id)

        if wait_for_results:
            scan_results = await wait_for_scan_results_async(self._client, scan_id=scan_id)
        else:
            scan_results = await get_scan_results_async(self._client, scan_id=scan_id)

        return scan_results

    async def scan_s3_model(
        self,
        *,
        model_name: str,
        bucket: str,
        key: str,
        model_version: str = "1",
        s3_client: Optional[object] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> "ScanReport":
        """
        Async version of scan_s3_model.

        See ModelScanner.scan_s3_model for parameter documentation.
        """
        try:
            import boto3  # type: ignore
        except ImportError as err:
            raise ImportError("Python package boto3 is not installed.") from err

        if not s3_client:
            s3_client = boto3.client("s3")  # type: ignore

        file_name = key.split("/")[-1]

        try:
            s3_client.download_file(bucket, key, f"/tmp/{file_name}")  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Couldn't download model s3://{bucket}/{key}: {e}") from e

        return await self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            model_version=model_version,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="S3",
        )

    async def scan_azure_blob_model(
        self,
        *,
        model_name: str,
        account_url: str,
        container: str,
        blob: str,
        model_version: str = "1",
        blob_service_client: Optional[object] = None,
        credential: Optional[object] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> "ScanReport":
        """
        Async version of scan_azure_blob_model.

        See ModelScanner.scan_azure_blob_model for parameter documentation.
        """
        try:
            from azure.identity import DefaultAzureCredential  # type: ignore
        except ImportError as err:
            raise ImportError("Python package azure-identity is not installed.") from err

        try:
            from azure.storage.blob import BlobServiceClient  # type: ignore
        except ImportError as err:
            raise ImportError("Python package azure-storage-blob is not installed.") from err

        if not credential:
            credential = DefaultAzureCredential()  # type: ignore

        if not blob_service_client:
            blob_service_client = BlobServiceClient(account_url, credential=credential)  # type: ignore

        file_name = blob.split("/")[-1]

        blob_client = blob_service_client.get_blob_client(  # type: ignore
            container=container, blob=blob
        )

        try:
            with open(os.path.join("/tmp", file_name), "wb") as f:
                download_stream = blob_client.download_blob()  # type: ignore
                f.write(download_stream.readall())  # type: ignore

        except Exception as e:
            raise RuntimeError(f"Couldn't download model {account_url}, {container}, {blob}: {e}") from e

        return await self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            model_version=model_version,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="Azure Blob Storage",
        )

    async def scan_huggingface_model(
        self,
        *,
        repo_id: str,
        model_name: Optional[str] = None,
        revision: Optional[str] = None,
        local_dir: str = "/tmp",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        force_download: bool = False,
        hf_token: Optional[Union[str, bool]] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> "ScanReport":
        """
        Async version of scan_huggingface_model.

        See ModelScanner.scan_huggingface_model for parameter documentation.
        """
        try:
            from huggingface_hub import snapshot_download  # type: ignore
        except ImportError as err:
            raise ImportError("Python package huggingface_hub is not installed.") from err

        local_dir = f"/tmp/{repo_id}" if local_dir == "/tmp" else local_dir
        ignore_file_patterns = EXCLUDE_FILE_TYPES + ignore_file_patterns if ignore_file_patterns else EXCLUDE_FILE_TYPES

        snapshot_download(
            repo_id,
            revision=revision,
            allow_patterns=allow_file_patterns,
            ignore_patterns=ignore_file_patterns,
            local_dir=local_dir,
            local_dir_use_symlinks=False,
            cache_dir=local_dir,
            force_download=force_download,
            token=hf_token,
        )

        if revision is None:
            revision = "1"

        return await self.scan_folder(
            model_name=model_name or repo_id,
            model_version=revision,
            path=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="Hugging Face",
        )

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

                response = await self._client._client.put(
                    part.upload_url,
                    content=part_data,
                    headers={"Content-Type": "application/octet-stream"},
                    timeout=self._client.timeout,
                )
                response.raise_for_status()

        # Complete the file upload
        await self._client.scans.upload.file.complete(file_id=upload.upload_id, scan_id=scan_id)
