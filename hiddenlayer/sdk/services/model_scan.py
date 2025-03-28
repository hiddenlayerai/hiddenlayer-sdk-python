import os
import random
import tempfile
import time
import zipfile
from pathlib import Path
from typing import Callable, List, Optional, Union

from hiddenlayer.sdk.constants import CommunityScanSource, ScanStatus
from hiddenlayer.sdk.models import EmptyScanResults, ScanResults
from hiddenlayer.sdk.rest.api import ModelSupplyChainApi
from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.exceptions import NotFoundException, UnauthorizedException
from hiddenlayer.sdk.rest.models import (
    MultiFileUploadRequestV3,
    ScanJob,
    ScanJobAccess,
    ScanModelDetailsV31,
)
from hiddenlayer.sdk.utils import filter_path_objects

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


class ModelScanAPI:
    def __init__(
        self,
        api_client: ApiClient,
        refresh_token_func: Optional[Callable[[], str]] = None,
    ) -> None:
        self._api_client = api_client
        self._model_supply_chain_api = ModelSupplyChainApi(api_client=api_client)
        self._refresh_token_func = refresh_token_func

    def community_scan(
        self,
        model_name: str,
        model_path: str,
        model_source: CommunityScanSource,
        model_version: str = "main",
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a model available at a remote location using the HiddenLayer Model Scanner.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param model_path: Path to the model file in the remote location, e.g. a presigned S3 URL
        :param model_source: type of remote location where the model is stored.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.

        :returns: Scan Results
        """
        scan_job = ScanJob(
            access=ScanJobAccess(source=model_source),
            inventory=ScanModelDetailsV31(
                model_name=model_name,
                model_version=model_version,
                requested_scan_location=model_path,
                requesting_entity="hiddenlayer-python-sdk",
            ),
        )
        result = self._model_supply_chain_api.create_scan_job(scan_job)
        scan_id = result.scan_id
        if scan_id is None:
            raise Exception("scan_id must have a value")
        if wait_for_results:
            return self._wait_for_scan_results(scan_id=scan_id)
        else:
            return ScanResults.from_scanreportv3(scan_report_v3=result)

    def scan_file(
        self,
        *,
        model_name: str,
        model_path: Union[str, os.PathLike],
        model_version: str = "1",
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a local model file using the HiddenLayer Model Scanner.

        :param model_name: Name of the model to be shown on the HiddenLayer UI
        :param model_path: Local path to the model file.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: Scan Results
        """

        file_path = Path(model_path)

        request = MultiFileUploadRequestV3(
            model_name=model_name,
            model_version=model_version,
            requesting_entity="hiddenlayer-python-sdk",
        )
        response = self._model_supply_chain_api.begin_multi_file_upload(
            multi_file_upload_request_v3=request
        )
        scan_id = response.scan_id
        if scan_id is None:
            raise Exception("scan_id must have a value")

        self._scan_file(scan_id=scan_id, file_path=file_path)

        self._model_supply_chain_api.complete_multi_file_upload(scan_id=scan_id)
        scan_results = self._wait_for_scan_results(scan_id=scan_id)
        scan_results.file_name = file_path.name
        scan_results.file_path = str(file_path)

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
    ) -> ScanResults:
        """
        Scan a model file on S3.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param bucket: Name of the s3 bucket where the model file is stored.
        :param key: Path to the model file on s3.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param s3_client: boto3 s3 client.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: Scan Results

        :examples:
            .. code-block:: python

                hl_client.model_scanner.scan_s3_model(
                    model_name="your-model-name",
                    bucket="s3_bucket",
                    key="path/to/file"
                )
        """
        try:
            import boto3  # type: ignore
        except ImportError:
            raise ImportError("Python package boto3 is not installed.")

        if not s3_client:
            s3_client = boto3.client("s3")

        file_name = key.split("/")[-1]

        try:
            s3_client.download_file(bucket, key, f"/tmp/{file_name}")  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Couldn't download model s3://{bucket}/{key}: {e}")

        return self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            model_version=model_version,
            wait_for_results=wait_for_results,
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
    ) -> ScanResults:
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
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: Scan Results

        :examples:
            .. code-block:: python

                hl_client.model_scanner.scan_azure_blob_model(
                    model_name="your-model-name",
                    account_url="https://<storageaccountname>.blob.core.windows.net",
                    container="container_name",
                    blob="path/to/file.bin",
                    credential="?<sas_key>" # If using a SAS key and not DefaultCredentials
                )
        """
        try:
            from azure.identity import DefaultAzureCredential
        except ImportError:
            raise ImportError("Python package azure-identity is not installed.")

        try:
            from azure.storage.blob import BlobServiceClient
        except ImportError:
            raise ImportError("Python package azure-storage-blob is not installed.")

        if not credential:
            credential = DefaultAzureCredential()

        if not blob_service_client:
            blob_service_client = BlobServiceClient(account_url, credential=credential)  # type: ignore

        file_name = blob.split("/")[-1]

        blob_client = blob_service_client.get_blob_client(  # type: ignore
            container=container, blob=blob
        )

        try:
            with open(os.path.join("/tmp", file_name), "wb") as f:
                download_stream = blob_client.download_blob()
                f.write(download_stream.readall())

        except Exception as e:
            raise RuntimeError(
                f"Couldn't download model {account_url}, {container}, {blob}: {e}"
            )

        return self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            model_version=model_version,
            wait_for_results=wait_for_results,
        )

    def scan_huggingface_model(
        self,
        *,
        repo_id: str,
        model_name: Optional[str] = None,
        # model_id: str,
        # HF parameters
        revision: Optional[str] = None,
        local_dir: str = "/tmp",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        force_download: bool = False,
        hf_token: Optional[Union[str, bool]] = None,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scans a model on HuggingFace.

        Note: Requires the `huggingface_hub` pip package to be installed.

        :param repo_id: The HuggingFace repository id.
        :param revision: An optional Git revision id which can be a branch name, a tag, or a commit hash.
        :param local_dir: If provided, the downloaded files will be placed under this directory.
        :param allow_file_patterns: If provided, only files matching at least one pattern are scanned.
        :param ignore_file_patterns: If provided, files matching any of the patterns are not scanned.
        :param force_download: Whether the file should be downloaded even if it already exists in the local cache.
        :param hf_token: A token to be used for the download.
            If True, the token is read from the HuggingFace config folder.
            If a string, it’s used as the authentication token.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: List of ScanResults
        """
        try:
            from huggingface_hub import snapshot_download
        except ImportError:
            raise ImportError("Python package huggingface_hub is not installed.")

        local_dir = f"/tmp/{repo_id}" if local_dir == "/tmp" else local_dir
        ignore_file_patterns = (
            EXCLUDE_FILE_TYPES + ignore_file_patterns
            if ignore_file_patterns
            else EXCLUDE_FILE_TYPES
        )

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
        )

    def get_scan_results(self, *, scan_id: str) -> ScanResults:
        """
        Get results from a model scan.

        :param model_name: Name of the model.
        :param model_version: Version of the model. When the model version is not specified, the scan results for the latest version will be returned.

        :returns: Scan results.
        """
        retry = False
        while True:
            try:
                scan_report = self._model_supply_chain_api.get_scan_results(scan_id)
                break
            except NotFoundException:
                return EmptyScanResults()
            except UnauthorizedException as e:
                if not retry and self._refresh_token_func:
                    new_token = self._refresh_token_func()
                    self._api_client.configuration.access_token = new_token
                    self._api_client = ApiClient(self._api_client.configuration)
                    retry = True
                else:
                    raise e

        return ScanResults.from_scanreportv3(scan_report_v3=scan_report)

    def get_sarif_results(
        self,
        *,
        scan_id: str,
    ) -> Optional[str]:
        """
        Get sarif results from a model scan.

        :param model_name: Name of the model.
        :param model_version: Version of the model. When the model version is not specified, the scan results for the latest version will be returned.

        :returns: Scan results.
        """

        # Unfortunately, the generated code for the API doesn't directly support modifying the Accept header
        # in order to enable us to get the Sarif results
        # Here we will reach in to the request serialization process. The 2nd element in the tuple is the headers
        # where we will modify the Accept header to application/sarif+json
        request = self._model_supply_chain_api._get_scan_results_serialize(
            scan_id, None, None, None, None, 0
        )
        request[2]["Accept"] = "application/sarif+json"
        response = self._api_client.call_api(*request)
        response.read()

        if response.data is None:
            return None

        return response.data.decode()

    def scan_folder(
        self,
        *,
        model_name: str,
        path: Union[str, os.PathLike],
        model_version: str = "1",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Submits all files in a directory and its sub directories to be scanned.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param path: Path to the folder on disk to be scanned.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param allow_file_patterns: If provided, only files matching at least one pattern are scanned.
        :param ignore_file_patterns: If provided, files matching any of the patterns are not scanned.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: List of ScanResults
        """

        model_path = Path(path)

        request = MultiFileUploadRequestV3(
            model_name=model_name,
            model_version=model_version,
            requesting_entity="hiddenlayer-python-sdk",
        )
        response = self._model_supply_chain_api.begin_multi_file_upload(
            multi_file_upload_request_v3=request
        )
        scan_id = response.scan_id
        if scan_id is None:
            raise Exception("scan_id must have a value")

        ignore_file_patterns = (
            EXCLUDE_FILE_TYPES + ignore_file_patterns
            if ignore_file_patterns
            else EXCLUDE_FILE_TYPES
        )

        files = filter_path_objects(
            model_path.rglob("*"),
            allow_patterns=allow_file_patterns,
            ignore_patterns=ignore_file_patterns,
        )

        for file in files:
            self._scan_file(scan_id=scan_id, file_path=Path(file))

        self._model_supply_chain_api.complete_multi_file_upload(scan_id=scan_id)
        scan_results = self._wait_for_scan_results(scan_id=scan_id)

        return scan_results

    def _scan_file(self, *, scan_id: str, file_path: Path):
        filesize = file_path.stat().st_size
        upload = self._model_supply_chain_api.begin_multipart_file_upload(
            scan_id=str(scan_id), file_name=str(file_path), file_content_length=filesize
        )

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
                self._api_client.call_api(
                    "PUT",
                    part.upload_url,
                    body=part_data,
                    header_params={"Content-Type": "application/octet-binary"},
                )
            self._model_supply_chain_api.complete_multipart_file_upload(
                scan_id=scan_id, file_id=upload.upload_id
            )

    def _wait_for_scan_results(self, *, scan_id: str):
        scan_results = self.get_scan_results(scan_id=scan_id)

        base_delay = 0.1  # seconds
        retries = 0
        print(f"scan status: {scan_results.status}")
        while scan_results.status not in [ScanStatus.DONE, ScanStatus.FAILED]:
            retries += 1
            delay = base_delay * 2**retries + random.uniform(
                0, 1
            )  # exponential back off retry
            delay = min(delay, 30)
            time.sleep(delay)
            scan_results = self.get_scan_results(scan_id=scan_id)
            print(f"scan status: {scan_results.status}")

        return scan_results
