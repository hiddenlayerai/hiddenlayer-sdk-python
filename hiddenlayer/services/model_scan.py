from hiddenlayer.rest.api.model_scan_api import ModelScanApi
from hiddenlayer.rest.api_client import ApiClient
from hiddenlayer.rest.api.sensor_api import SensorApi
from hiddenlayer.rest.models import (
    MultipartUploadPart,
    CreateSensorRequest,
)

import time
import os

from typing import Union, Optional, List

from pathlib import Path

from hiddenlayer.services.models import ScanResults


class ModelScanAPI:
    def __init__(self, api_client: ApiClient) -> None:
        self._model_scan_api = ModelScanApi(api_client=api_client)
        self._sensor_api = SensorApi(api_client=api_client)

    def scan_model_file(
        self,
        *,
        model_id: str,
        model_path: Union[str, os.PathLike],
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a local model file using the HiddenLayer Model Scanner.

        :param model_id: Name of the model to be shown on the HiddenLayer UI
        :param model_path: Local path to the model file.
        :param threads: Number of threads used to upload the file, defaults to 1.
        :param chunk_size: Number of chunks of the file to upload at once, defaults to 4.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.

        :returns: Scan Results
        """

        file_path = Path(model_path)

        filesize = file_path.stat().st_size
        sensor = self._sensor_api.create_sensor(
            CreateSensorRequest(plaintext_name=model_id)
        )

        upload = self._sensor_api.begin_multipart_upload(filesize, sensor.sensor_id)

        with open(file_path, "rb") as f:
            for i in range(0, len(upload.parts), chunk_size):
                group: List[MultipartUploadPart] = upload.parts[i : i + chunk_size]
                for part in group:
                    read_amount = part.end_offset - part.start_offset
                    f.seek(part.start_offset)
                    part_data = f.read(read_amount)
                    self._sensor_api.upload_model_part(
                        sensor_id=sensor.sensor_id,
                        upload_id=upload.upload_id,
                        part=part.part_number,
                        body=part_data,
                    )

        self._sensor_api.complete_multipart_upload(sensor.sensor_id, upload.upload_id)

        self._model_scan_api.scan_model(sensor.sensor_id)

        scan_results = self.get_scan_results(model_id=sensor.sensor_id)

        if wait_for_results:
            while scan_results.status not in ["done", "failed"]:
                time.sleep(5)
                scan_results = self.get_scan_results(model_id=sensor.sensor_id)
                print(f"Scan Status: {scan_results.status}")

        scan_results = ScanResults.from_scanresultsv2(scan_results_v2=scan_results)
        scan_results.file_name = file_path.name
        scan_results.file_path = str(file_path)

        return scan_results

    def scan_s3_model(
        self,
        *,
        model_id: str,
        bucket: str,
        key: str,
        s3_client: Optional[object] = None,
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> ScanResults:
        """
        Scan a model file on S3.

        :param model_id: Name of the model to be shown on the HiddenLayer UI.
        :param bucket: Name of the s3 bucket where the model file is stored.
        :param key: Path to the model file on s3.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param s3_client: boto3 s3 client.

        :returns: Scan Results
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

        return self.scan_model_file(
            model_path=f"/tmp/{file_name}",
            model_id=model_id,
            threads=threads,
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )

    def scan_huggingface_model(
        self,
        *,
        repo_id: str,
        model_id: str,
        revision: Optional[str] = None,
        local_dir: str = "/tmp",
        hf_token: Optional[str | bool] = None,
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ):
        try:
            from huggingface_hub import snapshot_download
        except ImportError:
            raise ImportError("Python package huggingface_hub is not installed.")

        snapshot_download(
            repo_id, revision=revision, local_dir=local_dir, token=hf_token
        )

        return self.scan_folder(
            path=local_dir,
            threads=threads,
            chunk_size=chunk_size,
            wait_for_results=wait_for_results,
        )

    def get_scan_results(self, *, model_id: str) -> ScanResults:
        """
        Get results from a model scan.

        :param sensor_id: ID of the model.

        :returns: Scan results.
        """
        scan_results_v2 = self._model_scan_api.scan_status(model_id)

        return ScanResults.from_scanresultsv2(scan_results_v2=scan_results_v2)

    def scan_folder(
        self,
        *,
        path: Union[str, os.PathLike],
        threads: int = 1,
        chunk_size: int = 4,
        wait_for_results: bool = True,
    ) -> List[ScanResults]:
        model_path = Path(path)

        files = model_path.rglob("*")

        return [
            self.scan_model_file(
                model_id=file.name,
                model_path=file,
                threads=threads,
                chunk_size=chunk_size,
                wait_for_results=wait_for_results,
            )
            for file in files
        ]
