"""Model scans of local files and folders, and of models in S3, Azure Blob Storage and Hugging Face.

Each scan uploads the files in parts to the URLs the API presigns, then reads the report.
"""

from __future__ import annotations

import logging
import os
from fnmatch import fnmatch
from pathlib import Path
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, Iterable, List, Optional, Set, Tuple, Union

import httpx
from ..errors.bad_request_error import BadRequestError
from ..scans.upload.file.types.add_file_response_parts_item import AddFileResponsePartsItem
from .scan_utils import (
    AsyncScanResultMixin,
    ScanReport,
    ScanResultMixin,
    get_scan_results,
    get_scan_results_async,
    wait_for_scan_results,
    wait_for_scan_results_async,
)

if TYPE_CHECKING:
    from ..client import AsyncHiddenLayer, HiddenLayer

logger = logging.getLogger(__name__)

REQUESTING_ENTITY = "hiddenlayer-python-sdk"

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

_UPLOAD_HEADERS = {"Content-Type": "application/octet-stream"}


def is_duplicate_file_error(exc: BadRequestError) -> bool:
    """Reports whether the API refused a file because the scan already has it."""
    body: object = exc.body
    if not isinstance(body, dict):
        return False
    detail = body.get("detail", "")
    return isinstance(detail, str) and "duplicate" in detail.lower()


def filter_path_objects(
    items: Iterable[PathInputType],
    *,
    allow_patterns: Optional[Union[List[str], str]] = None,
    ignore_patterns: Optional[Union[List[str], str]] = None,
) -> Generator[PathInputType, None, None]:
    """Yields the files among items that pass an allowlist and a denylist, each file once.

    Patterns are Unix shell-style wildcards, not regular expressions; see
    https://docs.python.org/3/library/fnmatch.html. Directories, unreadable paths and paths that
    resolve to a file already yielded, such as a symlink to it, are skipped.

    Args:
        items: Paths, as str or Path.
        allow_patterns: If given, a path must match at least one of these.
        ignore_patterns: If given, a path must match none of these.

    Raises:
        ValueError: If an item is neither a str nor a Path.
    """
    if isinstance(allow_patterns, str):
        allow_patterns = [allow_patterns]
    if isinstance(ignore_patterns, str):
        ignore_patterns = [ignore_patterns]

    seen: Set[str] = set()
    for item in items:
        if isinstance(item, str):
            path = Path(item)
        elif isinstance(item, Path):
            path = item
        else:
            raise ValueError("Objects must be string or Pathlike.")

        if path.is_dir():
            continue

        try:
            resolved = str(path.resolve())
        except OSError:
            logger.debug("Skipping inaccessible path: %s", path)
            continue
        if resolved in seen:
            logger.debug("Skipping duplicate file (same resolved path): %s", path)
            continue
        seen.add(resolved)

        if allow_patterns is not None and not any(fnmatch(str(path), pattern) for pattern in allow_patterns):
            continue
        if ignore_patterns is not None and any(fnmatch(str(path), pattern) for pattern in ignore_patterns):
            continue

        yield item


def _ignore_patterns(extra: Optional[List[str]]) -> List[str]:
    return EXCLUDE_FILE_TYPES + extra if extra else EXCLUDE_FILE_TYPES


def _read_part(file: BinaryIO, part: AddFileResponsePartsItem) -> Tuple[str, bytes]:
    """Returns a part's presigned URL and the bytes of the file that belong to it."""
    if part.start_offset is None:
        raise ValueError("part must have a start_offset")
    if part.upload_url is None:
        raise ValueError("part.upload_url must not be None")
    file.seek(part.start_offset)
    size = -1 if part.end_offset is None else part.end_offset - part.start_offset
    return part.upload_url, file.read(size)


def _upload_timeout(seconds: Optional[float]) -> Any:
    """The client's timeout, or a caller's own httpx client's when the client was given none."""
    return httpx.USE_CLIENT_DEFAULT if seconds is None else seconds


def _download_s3_model(*, bucket: str, key: str, s3_client: Optional[Any]) -> str:
    try:
        import boto3  # type: ignore[import-not-found, import-untyped, unused-ignore]
    except ImportError as err:
        raise ImportError("Python package boto3 is not installed.") from err

    if not s3_client:
        s3_client = boto3.client("s3")

    model_path = f"/tmp/{key.split('/')[-1]}"
    try:
        s3_client.download_file(bucket, key, model_path)
    except Exception as e:
        raise RuntimeError(f"Couldn't download model s3://{bucket}/{key}: {e}") from e
    return model_path


def _download_azure_blob_model(
    *,
    account_url: str,
    container: str,
    blob: str,
    blob_service_client: Optional[Any],
    credential: Optional[Any],
) -> str:
    try:
        from azure.identity import DefaultAzureCredential  # type: ignore[import-not-found, unused-ignore]
    except ImportError as err:
        raise ImportError("Python package azure-identity is not installed.") from err
    try:
        from azure.storage.blob import BlobServiceClient  # type: ignore[import-not-found, unused-ignore]
    except ImportError as err:
        raise ImportError("Python package azure-storage-blob is not installed.") from err

    if not credential:
        credential = DefaultAzureCredential()
    if not blob_service_client:
        blob_service_client = BlobServiceClient(account_url, credential=credential)

    blob_client = blob_service_client.get_blob_client(container=container, blob=blob)
    model_path = os.path.join("/tmp", blob.split("/")[-1])
    try:
        with open(model_path, "wb") as file:
            file.write(blob_client.download_blob().readall())
    except Exception as e:
        raise RuntimeError(f"Couldn't download model {account_url}, {container}, {blob}: {e}") from e
    return model_path


def _download_huggingface_model(
    *,
    repo_id: str,
    revision: Optional[str],
    local_dir: str,
    allow_file_patterns: Optional[List[str]],
    ignore_file_patterns: Optional[List[str]],
    force_download: bool,
    hf_token: Optional[Union[str, bool]],
) -> str:
    try:
        from huggingface_hub import snapshot_download  # type: ignore[import-not-found, unused-ignore]
    except ImportError as err:
        raise ImportError("Python package huggingface_hub is not installed.") from err

    local_dir = f"/tmp/{repo_id}" if local_dir == "/tmp" else local_dir
    snapshot_download(
        repo_id,
        revision=revision,
        allow_patterns=allow_file_patterns,
        ignore_patterns=_ignore_patterns(ignore_file_patterns),
        local_dir=local_dir,
        local_dir_use_symlinks=False,
        cache_dir=local_dir,
        force_download=force_download,
        token=hf_token,
    )
    return local_dir


class ModelScanner(ScanResultMixin):
    """Uploads model files to the HiddenLayer Model Scanner and returns the scan's report."""

    def __init__(self, client: "HiddenLayer") -> None:
        self._client = client

    def scan_file(
        self,
        *,
        model_name: str,
        model_path: PathInputType,
        model_version: str = "1",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> ScanReport:
        """Scans a local model file.

        Args:
            model_name: Name of the model, as shown in the HiddenLayer Console.
            model_path: Local path to the model file.
            model_version: Version of the model, as shown in the HiddenLayer Console.
            wait_for_results: Whether to wait for the scan to finish. When False, the report is
                returned as it stands.
            request_source: What requested the scan.
            origin: The platform the model came from.
        """
        scan_id = self._start_upload(
            model_name=model_name, model_version=model_version, request_source=request_source, origin=origin
        )
        self._scan_file(scan_id=scan_id, file_path=Path(model_path))
        return self._finish(scan_id=scan_id, wait_for_results=wait_for_results)

    def scan_folder(
        self,
        *,
        model_name: str,
        path: PathInputType,
        model_version: str = "1",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> ScanReport:
        """Scans every file in a folder and its subfolders as one model.

        Text, Markdown and lock files and anything under `.git` are always left out, and a file the
        scan already has is skipped.

        Args:
            model_name: Name of the model, as shown in the HiddenLayer Console.
            path: Path to the folder.
            model_version: Version of the model, as shown in the HiddenLayer Console.
            allow_file_patterns: If given, only files matching at least one pattern are scanned.
            ignore_file_patterns: If given, files matching any of these patterns aren't scanned.
            wait_for_results: Whether to wait for the scan to finish. When False, the report is
                returned as it stands.
            request_source: What requested the scan.
            origin: The platform the model came from.
        """
        scan_id = self._start_upload(
            model_name=model_name, model_version=model_version, request_source=request_source, origin=origin
        )
        files = filter_path_objects(
            Path(path).rglob("*"),
            allow_patterns=allow_file_patterns,
            ignore_patterns=_ignore_patterns(ignore_file_patterns),
        )
        for file in files:
            try:
                self._scan_file(scan_id=scan_id, file_path=Path(file))
            except BadRequestError as e:
                if not is_duplicate_file_error(e):
                    raise
                logger.warning("Duplicate file detected during folder scan, skipping: %s", file)
        return self._finish(scan_id=scan_id, wait_for_results=wait_for_results)

    def scan_s3_model(
        self,
        *,
        model_name: str,
        bucket: str,
        key: str,
        model_version: str = "1",
        s3_client: Optional[Any] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> ScanReport:
        """Downloads a model file from S3 to `/tmp` and scans it. Needs the `boto3` package.

        Args:
            model_name: Name of the model, as shown in the HiddenLayer Console.
            bucket: The S3 bucket the model file is in.
            key: The model file's key in the bucket.
            model_version: Version of the model, as shown in the HiddenLayer Console.
            s3_client: A boto3 S3 client. Defaults to `boto3.client("s3")`.
            wait_for_results: Whether to wait for the scan to finish.
            request_source: What requested the scan.

        Raises:
            ImportError: If boto3 isn't installed.
            RuntimeError: If the download fails.
        """
        model_path = _download_s3_model(bucket=bucket, key=key, s3_client=s3_client)
        return self.scan_file(
            model_path=model_path,
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
        blob_service_client: Optional[Any] = None,
        credential: Optional[Any] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> ScanReport:
        """Downloads a model file from Azure Blob Storage to `/tmp` and scans it.

        Needs the `azure-identity` and `azure-storage-blob` packages.

        Args:
            model_name: Name of the model, as shown in the HiddenLayer Console.
            account_url: The storage account's URL, e.g. `https://<account>.blob.core.windows.net`.
            container: The container the model file is in.
            blob: Path to the model file inside the container.
            model_version: Version of the model, as shown in the HiddenLayer Console.
            blob_service_client: A BlobServiceClient. Defaults to one built from account_url and credential.
            credential: A credential object, or a SAS token as `"?<sas>"`. Defaults to DefaultAzureCredential.
            wait_for_results: Whether to wait for the scan to finish.
            request_source: What requested the scan.

        Raises:
            ImportError: If either Azure package isn't installed.
            RuntimeError: If the download fails.
        """
        model_path = _download_azure_blob_model(
            account_url=account_url,
            container=container,
            blob=blob,
            blob_service_client=blob_service_client,
            credential=credential,
        )
        return self.scan_file(
            model_path=model_path,
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
    ) -> ScanReport:
        """Downloads a Hugging Face repository and scans it. Needs the `huggingface_hub` package.

        Args:
            repo_id: The Hugging Face repository ID.
            model_name: Name of the model, as shown in the HiddenLayer Console. Defaults to repo_id.
            revision: A branch name, tag or commit hash. Also the model version, which defaults to "1".
            local_dir: Where the files are downloaded. The default, `/tmp`, means `/tmp/<repo_id>`.
            allow_file_patterns: If given, only files matching at least one pattern are scanned.
            ignore_file_patterns: If given, files matching any of these patterns aren't scanned.
            force_download: Whether to download files that are already in the local cache.
            hf_token: A Hugging Face token, or True to read it from the Hugging Face config folder.
            wait_for_results: Whether to wait for the scan to finish.
            request_source: What requested the scan.

        Raises:
            ImportError: If huggingface_hub isn't installed.
        """
        local_dir = _download_huggingface_model(
            repo_id=repo_id,
            revision=revision,
            local_dir=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            force_download=force_download,
            hf_token=hf_token,
        )
        return self.scan_folder(
            model_name=model_name or repo_id,
            model_version="1" if revision is None else revision,
            path=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="Hugging Face",
        )

    def _start_upload(self, *, model_name: str, model_version: str, request_source: str, origin: str) -> str:
        return self._client.scans.upload.start(
            model_name=model_name,
            model_version=model_version,
            requesting_entity=REQUESTING_ENTITY,
            request_source=request_source,
            origin=origin,
        ).scan_id

    def _finish(self, *, scan_id: str, wait_for_results: bool) -> ScanReport:
        self._client.scans.upload.complete_all(scan_id)
        if wait_for_results:
            return wait_for_scan_results(self._client, scan_id=scan_id)
        return get_scan_results(self._client, scan_id=scan_id)

    def _scan_file(self, *, scan_id: str, file_path: Path) -> None:
        """Uploads one file to the scan, part by part."""
        upload = self._client.scans.upload.file.add(
            scan_id, file_name=str(file_path), file_content_length=file_path.stat().st_size
        )
        wrapper = self._client._client_wrapper
        with open(file_path, "rb") as file:
            for part in upload.parts:
                upload_url, data = _read_part(file, part)
                # Straight to the presigned URL on the client's httpx client, so no API credentials go with it.
                response = wrapper.httpx_client.httpx_client.put(
                    upload_url, content=data, headers=_UPLOAD_HEADERS, timeout=_upload_timeout(wrapper.get_timeout())
                )
                response.raise_for_status()
        self._client.scans.upload.file.complete(scan_id, upload.upload_id)


class AsyncModelScanner(AsyncScanResultMixin):
    """Async version of ModelScanner, for AsyncHiddenLayer."""

    def __init__(self, client: "AsyncHiddenLayer") -> None:
        self._client = client

    async def scan_file(
        self,
        *,
        model_name: str,
        model_path: PathInputType,
        model_version: str = "1",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> ScanReport:
        """Async version of ModelScanner.scan_file."""
        scan_id = await self._start_upload(
            model_name=model_name, model_version=model_version, request_source=request_source, origin=origin
        )
        await self._scan_file(scan_id=scan_id, file_path=Path(model_path))
        return await self._finish(scan_id=scan_id, wait_for_results=wait_for_results)

    async def scan_folder(
        self,
        *,
        model_name: str,
        path: PathInputType,
        model_version: str = "1",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> ScanReport:
        """Async version of ModelScanner.scan_folder."""
        scan_id = await self._start_upload(
            model_name=model_name, model_version=model_version, request_source=request_source, origin=origin
        )
        files = filter_path_objects(
            Path(path).rglob("*"),
            allow_patterns=allow_file_patterns,
            ignore_patterns=_ignore_patterns(ignore_file_patterns),
        )
        for file in files:
            try:
                await self._scan_file(scan_id=scan_id, file_path=Path(file))
            except BadRequestError as e:
                if not is_duplicate_file_error(e):
                    raise
                logger.warning("Duplicate file detected during folder scan, skipping: %s", file)
        return await self._finish(scan_id=scan_id, wait_for_results=wait_for_results)

    async def scan_s3_model(
        self,
        *,
        model_name: str,
        bucket: str,
        key: str,
        model_version: str = "1",
        s3_client: Optional[Any] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> ScanReport:
        """Async version of ModelScanner.scan_s3_model. The download itself blocks."""
        model_path = _download_s3_model(bucket=bucket, key=key, s3_client=s3_client)
        return await self.scan_file(
            model_path=model_path,
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
        blob_service_client: Optional[Any] = None,
        credential: Optional[Any] = None,
        wait_for_results: bool = True,
        request_source: str = "API Upload",
    ) -> ScanReport:
        """Async version of ModelScanner.scan_azure_blob_model. The download itself blocks."""
        model_path = _download_azure_blob_model(
            account_url=account_url,
            container=container,
            blob=blob,
            blob_service_client=blob_service_client,
            credential=credential,
        )
        return await self.scan_file(
            model_path=model_path,
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
    ) -> ScanReport:
        """Async version of ModelScanner.scan_huggingface_model. The download itself blocks."""
        local_dir = _download_huggingface_model(
            repo_id=repo_id,
            revision=revision,
            local_dir=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            force_download=force_download,
            hf_token=hf_token,
        )
        return await self.scan_folder(
            model_name=model_name or repo_id,
            model_version="1" if revision is None else revision,
            path=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            wait_for_results=wait_for_results,
            request_source=request_source,
            origin="Hugging Face",
        )

    async def _start_upload(self, *, model_name: str, model_version: str, request_source: str, origin: str) -> str:
        upload = await self._client.scans.upload.start(
            model_name=model_name,
            model_version=model_version,
            requesting_entity=REQUESTING_ENTITY,
            request_source=request_source,
            origin=origin,
        )
        return upload.scan_id

    async def _finish(self, *, scan_id: str, wait_for_results: bool) -> ScanReport:
        await self._client.scans.upload.complete_all(scan_id)
        if wait_for_results:
            return await wait_for_scan_results_async(self._client, scan_id=scan_id)
        return await get_scan_results_async(self._client, scan_id=scan_id)

    async def _scan_file(self, *, scan_id: str, file_path: Path) -> None:
        upload = await self._client.scans.upload.file.add(
            scan_id, file_name=str(file_path), file_content_length=file_path.stat().st_size
        )
        wrapper = self._client._client_wrapper
        with open(file_path, "rb") as file:
            for part in upload.parts:
                upload_url, data = _read_part(file, part)
                response = await wrapper.httpx_client.httpx_client.put(
                    upload_url, content=data, headers=_UPLOAD_HEADERS, timeout=_upload_timeout(wrapper.get_timeout())
                )
                response.raise_for_status()
        await self._client.scans.upload.file.complete(scan_id, upload.upload_id)
