import json
import os
import random
import tempfile
import time
import warnings
import zipfile
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Union
from uuid import uuid4

from pydantic_core import ValidationError

from hiddenlayer.sdk.constants import ScanStatus
from hiddenlayer.sdk.models import EmptyScanResults, Sarif, ScanResults
from hiddenlayer.sdk.rest.api import ModelScanApi, ModelSupplyChainApi, SensorApi
from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.models import MultipartUploadPart
from hiddenlayer.sdk.rest.models.model import Model
from hiddenlayer.sdk.rest.models.sarif210 import Sarif210
from hiddenlayer.sdk.services.model import ModelAPI
from hiddenlayer.sdk.utils import filter_path_objects, is_saas

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
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

        self._model_supply_chain_api = ModelSupplyChainApi(api_client=api_client)
        self._model_api = ModelAPI(api_client=api_client)
        self._sensor_api = SensorApi(
            api_client=api_client
        )  # lower level api of ModelAPI

        self._model_scan_api = ModelScanApi(api_client=api_client)

    def scan_file(
        self,
        *,
        model_name: str,
        model_path: Union[str, os.PathLike],
        model_version: Optional[int] = None,
        chunk_size: int = 16,
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

        filesize = file_path.stat().st_size
        sensor = self._model_api.create(
            model_name=model_name, model_version=model_version
        )
        upload = self._sensor_api.begin_multipart_upload(sensor.sensor_id, filesize)

        with open(file_path, "rb") as f:
            for i in range(0, len(upload.parts), chunk_size):
                group: List[MultipartUploadPart] = upload.parts[i : i + chunk_size]
                for part in group:
                    read_amount = part.end_offset - part.start_offset
                    f.seek(int(part.start_offset))
                    part_data = f.read(int(read_amount))

                    # The SaaS multipart upload returns a upload url for each part
                    # So there is no specified route
                    self._api_client.call_api(
                        "PUT",
                        part.upload_url,
                        body=part_data,
                        header_params={"Content-Type": "application/octet-binary"},
                    )

        self._sensor_api.complete_multipart_upload(sensor.sensor_id, upload.upload_id)

        self._model_scan_api.scan_model(sensor.sensor_id)

        scan_results = self.get_scan_results(
            model_name=model_name, model_version=model_version
        )

        base_delay = 0.1  # seconds
        retries = 0
        if wait_for_results:
            print(f"{file_path.name} scan status: {scan_results.status}")
            while scan_results.status not in [ScanStatus.DONE, ScanStatus.FAILED]:
                retries += 1
                delay = base_delay * 2**retries + random.uniform(
                    0, 1
                )  # exponential back off retry
                time.sleep(delay)
                scan_results = self.get_scan_results(
                    model_name=model_name, model_version=model_version
                )
                print(f"{file_path.name} scan status: {scan_results.status}")

        scan_results.file_name = file_path.name
        scan_results.file_path = str(file_path)

        return scan_results

    def scan_s3_model(
        self,
        *,
        model_name: str,
        bucket: str,
        key: str,
        model_version: Optional[int] = None,
        s3_client: Optional[object] = None,
        chunk_size: int = 4,
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
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )

    def scan_azure_blob_model(
        self,
        *,
        model_name: str,
        account_url: str,
        container: str,
        blob: str,
        model_version: Optional[int] = None,
        blob_service_client: Optional[object] = None,
        credential: Optional[object] = None,
        chunk_size: int = 4,
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
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )

    def scan_huggingface_model(
        self,
        *,
        repo_id: str,
        # model_id: str,
        # HF parameters
        revision: Optional[str] = None,
        local_dir: str = "/tmp",
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        force_download: bool = False,
        hf_token: Optional[Union[str, bool]] = None,
        # HL parameters
        chunk_size: int = 4,
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

        return self.scan_folder(
            model_name=repo_id,
            path=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )

    def get_scan_results(
        self,
        *,
        model_name: str,
        model_version: Optional[int] = None,
    ) -> ScanResults:
        """
        Get results from a model scan.

        :param model_name: Name of the model.
        :param model_version: Version of the model. When the model version is not specified, the scan results for the latest version will be returned.

        :returns: Scan results.
        """

        response = self._sensor_api.sensor_sor_api_v3_model_cards_query_get(
            model_name_eq=model_name, limit=1
        )
        model_id = response.results[0].model_id

        scans = self._model_supply_chain_api.model_scan_api_v3_scan_query(
            model_ids=[model_id], latest_per_model_version_only=True
        )
        if scans.total == 0:
            return EmptyScanResults()

        if scans.items is None:
            return EmptyScanResults()

        scan = scans.items[0]
        if model_version:
            scan = next(
                (
                    s
                    for s in scans.items
                    if s.inventory.model_version == str(model_version)
                ),
                None,
            )
        if not scan:
            return EmptyScanResults()

        scan_report = (
            self._model_supply_chain_api.model_scan_api_v3_scan_model_version_id_get(
                scan.scan_id
            )
        )

        return ScanResults.from_scanreportv3(
            scan_report_v3=scan_report, model_id=model_id
        )

    def get_sarif_results(
        self,
        *,
        model_name: str,
        model_version: Optional[int] = None,
    ) -> Optional[Sarif]:
        """
        Get sarif results from a model scan.

        :param model_name: Name of the model.
        :param model_version: Version of the model. When the model version is not specified, the scan results for the latest version will be returned.

        :returns: Scan results.
        """
        scan = self.get_scan_results(model_name=model_name, model_version=model_version)
        if scan.scan_id == "":
            return None

        # Unfortunately, the generated code for the API doesn't directly support modifying the Accept header
        # in order to enable us to get the Sarif results
        # Here we will reach in to the request serialization process. The 2nd element in the tuple is the headers
        # where we will modify the Accept header to application/sarif+json
        request = self._model_supply_chain_api._model_scan_api_v3_scan_model_version_id_get_serialize(
            scan.scan_id, None, None, None, None, 0
        )
        request[2]["Accept"] = "application/sarif+json"
        response = self._api_client.call_api(*request)
        response.read()
        return self._api_client.response_deserialize(
            response_data=response, response_types_map={"200": Sarif}
        ).data  # type: ignore

    def scan_folder(
        self,
        *,
        model_name: str,
        path: Union[str, os.PathLike],
        model_version: Optional[int] = None,
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        chunk_size: int = 4,
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
        filename = tempfile.NamedTemporaryFile().name + ".zip"

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

        with zipfile.ZipFile(filename, "a") as zipf:
            for file in files:
                zipf.write(file, os.path.relpath(file, model_path))

        return self.scan_file(
            model_name=model_name,
            model_version=model_version,
            model_path=filename,
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )
