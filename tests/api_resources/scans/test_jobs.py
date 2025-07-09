# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types.scans import ScanJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_request(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_request_with_all_params(self, client: HiddenLayer) -> None:
        job = client.scans.jobs.request(
            access={"source": "HUGGING_FACE"},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
                "origin": "Hugging Face",
                "request_source": "API Upload",
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_request(self, client: HiddenLayer) -> None:
        response = client.scans.jobs.with_raw_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_request(self, client: HiddenLayer) -> None:
        with client.scans.jobs.with_streaming_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_request(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_request_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        job = await async_client.scans.jobs.request(
            access={"source": "HUGGING_FACE"},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
                "origin": "Hugging Face",
                "request_source": "API Upload",
            },
        )
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_request(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.jobs.with_raw_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ScanJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.jobs.with_streaming_response.request(
            access={},
            inventory={
                "model_name": "some-model",
                "model_version": "",
                "requested_scan_location": "owner/repo",
                "requesting_entity": "some-user@example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ScanJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True
