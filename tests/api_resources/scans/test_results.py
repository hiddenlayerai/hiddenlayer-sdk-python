# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer._utils import parse_datetime
from hiddenlayer.types.scans import (
    ScanReport,
    ResultListResponse,
    ResultPatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: HiddenLayer) -> None:
        result = client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            has_detections=True,
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ScanReport, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.results.with_raw_response.retrieve(
                scan_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: HiddenLayer) -> None:
        result = client.scans.results.list()
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            latest_per_model_version_only=True,
            limit=1,
            model_ids=["string"],
            model_version_ids=["string"],
            offset=0,
            severity=["string"],
            sort="sort",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["string"],
        )
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultListResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_patch(self, client: HiddenLayer) -> None:
        result = client.scans.results.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )
        assert_matches_type(ResultPatchResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_patch_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
                "model_source": "adhoc",
                "requesting_entity": "requesting_entity",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
            has_detections=True,
            detection_categories=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_results=[
                {
                    "details": {
                        "estimated_time": "estimated_time",
                        "file_type": "safetensors",
                        "sha256": "a54d88e06612d820bc3be72877c74f257b561b19",
                        "file_size": "9 GB",
                        "file_size_bytes": 9663676416,
                        "file_type_details": {"foo": "bar"},
                        "md5": "ce114e4501d2f4e2dcea3e17b546f339",
                        "tlsh": "T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293",
                    },
                    "end_time": parse_datetime("2024-10-16T23:38:32.354Z"),
                    "file_instance_id": "file_instance_id",
                    "file_location": "file_location",
                    "seen": parse_datetime("2024-10-22T17:59:12.431Z"),
                    "start_time": parse_datetime("2024-10-16T23:38:32.278Z"),
                    "status": "skipped",
                    "detections": [
                        {
                            "category": "Arbitrary Code Execution",
                            "description": "Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution",
                            "detection_id": "00000000-0000-0000-0000-000000000000",
                            "mitre_atlas": [
                                {
                                    "tactic": "AML.TA0001",
                                    "technique": "AML.T0003.45",
                                }
                            ],
                            "owasp": ["LLM21"],
                            "rule_id": "PICKLE_0055_202408",
                            "severity": "low",
                            "cve": ["CVE-7321-910225"],
                            "cwe": "",
                            "cwe_href": "cwe_href",
                            "impact": "critical",
                            "likelihood": "medium",
                            "risk": "MALICIOUS",
                            "rule_details": [
                                {
                                    "description": "description",
                                    "status": "created",
                                    "status_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                }
                            ],
                            "technical_blog_href": "technical_blog_href",
                        }
                    ],
                    "file_results": [],
                }
            ],
            severity="low",
        )
        assert_matches_type(ResultPatchResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_patch(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultPatchResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_patch(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultPatchResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_patch(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_scan_id` but received ''"):
            client.scans.results.with_raw_response.patch(
                path_scan_id="",
                detection_count=0,
                file_count=0,
                files_with_detections_count=0,
                inventory={
                    "model_id": "00000000-0000-0000-0000-000000000000",
                    "model_name": "keras-tf-2025-05-27",
                    "model_version": "1.0.0",
                    "model_version_id": "00000000-0000-0000-0000-000000000000",
                    "requested_scan_location": "/files-to-scan",
                },
                body_scan_id="scan_id",
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                status="pending",
                version="version",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_start(self, client: HiddenLayer) -> None:
        result = client.scans.results.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )
        assert result is None

    @pytest.mark.skip()
    @parametrize
    def test_method_start_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
                "model_source": "adhoc",
                "requesting_entity": "requesting_entity",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
            has_detections=True,
            detection_categories=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_results=[
                {
                    "details": {
                        "estimated_time": "estimated_time",
                        "file_type": "safetensors",
                        "sha256": "a54d88e06612d820bc3be72877c74f257b561b19",
                        "file_size": "9 GB",
                        "file_size_bytes": 9663676416,
                        "file_type_details": {"foo": "bar"},
                        "md5": "ce114e4501d2f4e2dcea3e17b546f339",
                        "tlsh": "T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293",
                    },
                    "end_time": parse_datetime("2024-10-16T23:38:32.354Z"),
                    "file_instance_id": "file_instance_id",
                    "file_location": "file_location",
                    "seen": parse_datetime("2024-10-22T17:59:12.431Z"),
                    "start_time": parse_datetime("2024-10-16T23:38:32.278Z"),
                    "status": "skipped",
                    "detections": [
                        {
                            "category": "Arbitrary Code Execution",
                            "description": "Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution",
                            "detection_id": "00000000-0000-0000-0000-000000000000",
                            "mitre_atlas": [
                                {
                                    "tactic": "AML.TA0001",
                                    "technique": "AML.T0003.45",
                                }
                            ],
                            "owasp": ["LLM21"],
                            "rule_id": "PICKLE_0055_202408",
                            "severity": "low",
                            "cve": ["CVE-7321-910225"],
                            "cwe": "",
                            "cwe_href": "cwe_href",
                            "impact": "critical",
                            "likelihood": "medium",
                            "risk": "MALICIOUS",
                            "rule_details": [
                                {
                                    "description": "description",
                                    "status": "created",
                                    "status_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                }
                            ],
                            "technical_blog_href": "technical_blog_href",
                        }
                    ],
                    "file_results": [],
                }
            ],
            severity="low",
        )
        assert result is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_start(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert result is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_start(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert result is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_start(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_scan_id` but received ''"):
            client.scans.results.with_raw_response.start(
                path_scan_id="",
                detection_count=0,
                file_count=0,
                files_with_detections_count=0,
                inventory={
                    "model_id": "00000000-0000-0000-0000-000000000000",
                    "model_name": "keras-tf-2025-05-27",
                    "model_version": "1.0.0",
                    "model_version_id": "00000000-0000-0000-0000-000000000000",
                    "requested_scan_location": "/files-to-scan",
                },
                body_scan_id="scan_id",
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                status="pending",
                version="version",
            )


class TestAsyncResults:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            has_detections=True,
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ScanReport, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.results.with_raw_response.retrieve(
                scan_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.list()
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            latest_per_model_version_only=True,
            limit=1,
            model_ids=["string"],
            model_version_ids=["string"],
            offset=0,
            severity=["string"],
            sort="sort",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["string"],
        )
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultListResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_patch(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )
        assert_matches_type(ResultPatchResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
                "model_source": "adhoc",
                "requesting_entity": "requesting_entity",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
            has_detections=True,
            detection_categories=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_results=[
                {
                    "details": {
                        "estimated_time": "estimated_time",
                        "file_type": "safetensors",
                        "sha256": "a54d88e06612d820bc3be72877c74f257b561b19",
                        "file_size": "9 GB",
                        "file_size_bytes": 9663676416,
                        "file_type_details": {"foo": "bar"},
                        "md5": "ce114e4501d2f4e2dcea3e17b546f339",
                        "tlsh": "T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293",
                    },
                    "end_time": parse_datetime("2024-10-16T23:38:32.354Z"),
                    "file_instance_id": "file_instance_id",
                    "file_location": "file_location",
                    "seen": parse_datetime("2024-10-22T17:59:12.431Z"),
                    "start_time": parse_datetime("2024-10-16T23:38:32.278Z"),
                    "status": "skipped",
                    "detections": [
                        {
                            "category": "Arbitrary Code Execution",
                            "description": "Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution",
                            "detection_id": "00000000-0000-0000-0000-000000000000",
                            "mitre_atlas": [
                                {
                                    "tactic": "AML.TA0001",
                                    "technique": "AML.T0003.45",
                                }
                            ],
                            "owasp": ["LLM21"],
                            "rule_id": "PICKLE_0055_202408",
                            "severity": "low",
                            "cve": ["CVE-7321-910225"],
                            "cwe": "",
                            "cwe_href": "cwe_href",
                            "impact": "critical",
                            "likelihood": "medium",
                            "risk": "MALICIOUS",
                            "rule_details": [
                                {
                                    "description": "description",
                                    "status": "created",
                                    "status_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                }
                            ],
                            "technical_blog_href": "technical_blog_href",
                        }
                    ],
                    "file_results": [],
                }
            ],
            severity="low",
        )
        assert_matches_type(ResultPatchResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultPatchResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.patch(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultPatchResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_patch(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_scan_id` but received ''"):
            await async_client.scans.results.with_raw_response.patch(
                path_scan_id="",
                detection_count=0,
                file_count=0,
                files_with_detections_count=0,
                inventory={
                    "model_id": "00000000-0000-0000-0000-000000000000",
                    "model_name": "keras-tf-2025-05-27",
                    "model_version": "1.0.0",
                    "model_version_id": "00000000-0000-0000-0000-000000000000",
                    "requested_scan_location": "/files-to-scan",
                },
                body_scan_id="scan_id",
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                status="pending",
                version="version",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_start(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )
        assert result is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
                "model_source": "adhoc",
                "requesting_entity": "requesting_entity",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
            has_detections=True,
            detection_categories=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_results=[
                {
                    "details": {
                        "estimated_time": "estimated_time",
                        "file_type": "safetensors",
                        "sha256": "a54d88e06612d820bc3be72877c74f257b561b19",
                        "file_size": "9 GB",
                        "file_size_bytes": 9663676416,
                        "file_type_details": {"foo": "bar"},
                        "md5": "ce114e4501d2f4e2dcea3e17b546f339",
                        "tlsh": "T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293",
                    },
                    "end_time": parse_datetime("2024-10-16T23:38:32.354Z"),
                    "file_instance_id": "file_instance_id",
                    "file_location": "file_location",
                    "seen": parse_datetime("2024-10-22T17:59:12.431Z"),
                    "start_time": parse_datetime("2024-10-16T23:38:32.278Z"),
                    "status": "skipped",
                    "detections": [
                        {
                            "category": "Arbitrary Code Execution",
                            "description": "Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution",
                            "detection_id": "00000000-0000-0000-0000-000000000000",
                            "mitre_atlas": [
                                {
                                    "tactic": "AML.TA0001",
                                    "technique": "AML.T0003.45",
                                }
                            ],
                            "owasp": ["LLM21"],
                            "rule_id": "PICKLE_0055_202408",
                            "severity": "low",
                            "cve": ["CVE-7321-910225"],
                            "cwe": "",
                            "cwe_href": "cwe_href",
                            "impact": "critical",
                            "likelihood": "medium",
                            "risk": "MALICIOUS",
                            "rule_details": [
                                {
                                    "description": "description",
                                    "status": "created",
                                    "status_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                }
                            ],
                            "technical_blog_href": "technical_blog_href",
                        }
                    ],
                    "file_results": [],
                }
            ],
            severity="low",
        )
        assert result is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert result is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.start(
            path_scan_id="00000000-0000-0000-0000-000000000000",
            detection_count=0,
            file_count=0,
            files_with_detections_count=0,
            inventory={
                "model_id": "00000000-0000-0000-0000-000000000000",
                "model_name": "keras-tf-2025-05-27",
                "model_version": "1.0.0",
                "model_version_id": "00000000-0000-0000-0000-000000000000",
                "requested_scan_location": "/files-to-scan",
            },
            body_scan_id="scan_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            version="version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert result is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_start(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_scan_id` but received ''"):
            await async_client.scans.results.with_raw_response.start(
                path_scan_id="",
                detection_count=0,
                file_count=0,
                files_with_detections_count=0,
                inventory={
                    "model_id": "00000000-0000-0000-0000-000000000000",
                    "model_name": "keras-tf-2025-05-27",
                    "model_version": "1.0.0",
                    "model_version_id": "00000000-0000-0000-0000-000000000000",
                    "requested_scan_location": "/files-to-scan",
                },
                body_scan_id="scan_id",
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                status="pending",
                version="version",
            )
