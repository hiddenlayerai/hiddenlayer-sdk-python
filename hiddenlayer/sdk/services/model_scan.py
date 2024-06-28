import os
import random
import time
import warnings
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Union
from uuid import uuid4

from hiddenlayer.sdk.constants import ScanStatus
from hiddenlayer.sdk.enterprise.enterprise_model_scan_api import EnterpriseModelScanApi
from hiddenlayer.sdk.models import ScanResults
from hiddenlayer.sdk.rest.api import ModelScanApi, SensorApi
from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.models import MultipartUploadPart
from hiddenlayer.sdk.rest.models.model import Model
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
        self.is_saas = is_saas(api_client.configuration.host)
        self._api_client = api_client

        if self.is_saas:
            self._model_scan_api = ModelScanApi(api_client=api_client)
            self._model_api = ModelAPI(api_client=api_client)
            self._sensor_api = SensorApi(
                api_client=api_client
            )  # lower level api of ModelAPI
        else:
            self._model_scan_api = EnterpriseModelScanApi(api_client=api_client)

    def scan_file(
        self,
        *,
        model_name: str,
        model_path: Union[str, os.PathLike],
        threads: int = 1,
        chunk_size: int = 16,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a local model file using the HiddenLayer Model Scanner.

        :param model_name: Name of the model to be shown on the HiddenLayer UI
        :param model_path: Local path to the model file.
        :param threads: Number of threads used to upload the file, defaults to 1.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: Scan Results
        """

        warnings.warn(
            "Use of the threads parameter is deprecated and will be removed in version 0.2.0.",
            category=DeprecationWarning,
            stacklevel=2,
        )

        file_path = Path(model_path)

        # Can combine the 2 paths when SaaS API and Enterprise APIs are in sync
        if self.is_saas:
            filesize = file_path.stat().st_size
            sensor = self._model_api.create(model_name=model_name)
            upload = self._sensor_api.begin_multipart_upload(filesize, sensor.sensor_id)

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

            self._sensor_api.complete_multipart_upload(
                sensor.sensor_id, upload.upload_id
            )

            self._model_scan_api.scan_model(sensor.sensor_id)
        else:
            with open(file_path, "rb") as f:
                data = f.read()

            sensor = Model(
                sensor_id=str(uuid4()),
                created_at=datetime.now(),
                tenant_id="0000",
                plaintext_name=model_name,
                active=True,
                version=1,
            )

            self._model_scan_api: EnterpriseModelScanApi
            self._model_scan_api.scan_model(sensor.sensor_id, data)
            model_name = sensor.sensor_id

        scan_results = self.get_scan_results(model_name=model_name)

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
                scan_results = self.get_scan_results(model_name=model_name)
                print(f"{file_path.name} scan status: {scan_results.status}")

        scan_results = ScanResults.from_scanresultsv2(scan_results_v2=scan_results)
        scan_results.file_name = file_path.name
        scan_results.file_path = str(file_path)
        scan_results.sensor_id = sensor.sensor_id

        return scan_results

    def scan_s3_model(
        self,
        *,
        model_name: str,
        bucket: str,
        key: str,
        s3_client: Optional[object] = None,
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a model file on S3.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param bucket: Name of the s3 bucket where the model file is stored.
        :param key: Path to the model file on s3.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param s3_client: boto3 s3 client.
        :param threads: Number of threads used to upload the file, defaults to 1.
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
            import boto3
        except ImportError:
            raise ImportError("Python package boto3 is not installed.")

        if not s3_client:
            s3_client = boto3.client("s3")

        file_name = key.split("/")[-1]

        try:
            s3_client.download_file(bucket, key, f"/tmp/{file_name}")
        except Exception as e:
            raise RuntimeError(f"Couldn't download model s3://{bucket}/{key}: {e}")

        return self.scan_file(
            model_path=f"/tmp/{file_name}",
            model_name=model_name,
            threads=threads,
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
        blob_service_client: Optional[object] = None,
        credential: Optional[object] = None,
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a model file on Azure Blob Storage.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param account_url: Azure Blob url of where the file is stored.
        :param container: Azure Blob container containing the model file.
        :param blob: Path to the model file inside the Azure blob container.
        :param blob_service_client: BlobServiceClient object. Defaults to creating one using DefaultCredential().
        :param credential: Credential to be passed to the BlobServiceClient object, can be a credential object, SAS key, etc.
            Defaults to `DefaultCredential`
        :param threads: Number of threads used to upload the file, defaults to 1.
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
            blob_service_client = BlobServiceClient(account_url, credential=credential)

        file_name = blob.split("/")[-1]

        blob_client = blob_service_client.get_blob_client(
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
            threads=threads,
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
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> List[ScanResults]:
        """
        Scans a model on HuggingFace.

        Note: Requires the `huggingface_hub` pip package to be installed.

        :param revision: An optional Git revision id which can be a branch name, a tag, or a commit hash.
        :param local_dir: If provided, the downloaded files will be placed under this directory.
        :param allow_file_patterns: If provided, only files matching at least one pattern are scanned.
        :param ignore_file_patterns: If provided, files matching any of the patterns are not scanned.
        :param force_download: Whether the file should be downloaded even if it already exists in the local cache.
        :param hf_token: A token to be used for the download.
            If True, the token is read from the HuggingFace config folder.
            If a string, it’s used as the authentication token.
        :param threads: Number of threads used to upload the file, defaults to 1.
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
            path=local_dir,
            allow_file_patterns=allow_file_patterns,
            ignore_file_patterns=ignore_file_patterns,
            threads=threads,
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )

    def get_scan_results(self, *, model_name: str) -> ScanResults:
        """
        Get results from a model scan.

        :param model_name: Name of the model.

        :returns: Scan results.
        """

        if self.is_saas:
            model = self._model_api.get(model_name=model_name)
            sensor_id = model.sensor_id
        else:
            sensor_id = model_name

        scan_results_v2 = self._model_scan_api.scan_status(sensor_id)

        return ScanResults.from_scanresultsv2(
            scan_results_v2=scan_results_v2, sensor_id=sensor_id
        )

    def scan_folder(
        self,
        *,
        path: Union[str, os.PathLike],
        allow_file_patterns: Optional[List[str]] = None,
        ignore_file_patterns: Optional[List[str]] = None,
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> List[ScanResults]:
        """
        Submits all files in a directory and its sub directories to be scanned.

        :param path: Path to the folder on disk to be scanned.
        :param allow_file_patterns: If provided, only files matching at least one pattern are scanned.
        :param ignore_file_patterns: If provided, files matching any of the patterns are not scanned.
        :param threads: Number of threads used to upload the file, defaults to 1.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: List of ScanResults
        """

        model_path = Path(path)
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

        return [
            self.scan_file(
                model_name=str(file),
                model_path=file,
                threads=threads,
                chunk_size=chunk_size,
                wait_for_results=wait_for_results,
            )
            for file in files
        ]
