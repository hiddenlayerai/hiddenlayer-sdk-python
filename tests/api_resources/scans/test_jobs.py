# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer._utils import parse_datetime
from hiddenlayer.types.scans import (
    ScanJob,
    ScanReport,
    JobListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReport, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            has_detections=True,
        )
        assert_matches_type(ScanReport, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HiddenLayer) -> None:
        response = client.scans.jobs.with_raw_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ScanReport, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HiddenLayer) -> None:
        with client.scans.jobs.with_streaming_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ScanReport, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.jobs.with_raw_response.retrieve(
                scan_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.list(
            compliance_status=["COMPLIANT"],
            deep_scan=True,
            detection_category="detection_category",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            latest_per_model_version_only=True,
            limit=1,
            model_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            model_name={
                "contains": "contains",
                "eq": "eq",
            },
            model_version_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            offset=0,
            provider=["string"],
            region=["string"],
            request_source=["Hybrid Upload"],
            scanner_version="891.0.97194",
            severity="critical",
            sort="-region",
            source={"eq": "adhoc"},
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["string"],
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HiddenLayer) -> None:
        response = client.scans.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HiddenLayer) -> None:
        with client.scans.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_request(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_request_with_all_params(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.request(
            access={"source": "HUGGING_FACE"},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
                "origin": "Hugging Face",
                "request_source": "Hybrid Upload",
                "requested_scan_location": "owner/repo",
                "scan_target": {
                    "asset_region": "us-east-1",
                    "deep_scan": {
                        "file_location": "https://huggingface.co/meta-llama/Llama-3.1-8B",
                        "files": [
                            {
                                "file_location": "https://huggingface.co/meta-llama/Llama-3.1-8B/resolve/main/config.json",
                                "file_name_alias": "model-config.json",
                            }
                        ],
                    },
                    "provider_details": {
                        "provider": "AWS_BEDROCK",
                        "provider_model_id": "anthropic.claude-3-5-sonnet-20241022-v2:0",
                        "model_arn": "arn:aws:bedrock:us-east-1:123456789012:provisioned-model/my-custom-model",
                    },
                },
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_request(self, client: HiddenLayer) -> None:
        response = client.scans.jobs.with_raw_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_request(self, client: HiddenLayer) -> None:
        with client.scans.jobs.with_streaming_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ScanJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReport, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            has_detections=True,
        )
        assert_matches_type(ScanReport, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.jobs.with_raw_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ScanReport, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.jobs.with_streaming_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ScanReport, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.jobs.with_raw_response.retrieve(
                scan_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.list(
            compliance_status=["COMPLIANT"],
            deep_scan=True,
            detection_category="detection_category",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            latest_per_model_version_only=True,
            limit=1,
            model_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            model_name={
                "contains": "contains",
                "eq": "eq",
            },
            model_version_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            offset=0,
            provider=["string"],
            region=["string"],
            request_source=["Hybrid Upload"],
            scanner_version="891.0.97194",
            severity="critical",
            sort="-region",
            source={"eq": "adhoc"},
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["string"],
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_request(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_request_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.request(
            access={"source": "HUGGING_FACE"},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
                "origin": "Hugging Face",
                "request_source": "Hybrid Upload",
                "requested_scan_location": "owner/repo",
                "scan_target": {
                    "asset_region": "us-east-1",
                    "deep_scan": {
                        "file_location": "https://huggingface.co/meta-llama/Llama-3.1-8B",
                        "files": [
                            {
                                "file_location": "https://huggingface.co/meta-llama/Llama-3.1-8B/resolve/main/config.json",
                                "file_name_alias": "model-config.json",
                            }
                        ],
                    },
                    "provider_details": {
                        "provider": "AWS_BEDROCK",
                        "provider_model_id": "anthropic.claude-3-5-sonnet-20241022-v2:0",
                        "model_arn": "arn:aws:bedrock:us-east-1:123456789012:provisioned-model/my-custom-model",
                    },
                },
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_request(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.jobs.with_raw_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.jobs.with_streaming_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requesting_entity": "some-user@example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ScanJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True
