# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types.scans import UploadStartResponse, UploadCompleteAllResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete_all(self, client: HiddenLayer) -> None:
        upload = client.scans.upload.complete_all(
            "00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(UploadCompleteAllResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete_all(self, client: HiddenLayer) -> None:
        response = client.scans.upload.with_raw_response.complete_all(
            "00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadCompleteAllResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete_all(self, client: HiddenLayer) -> None:
        with client.scans.upload.with_streaming_response.complete_all(
            "00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadCompleteAllResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_complete_all(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.upload.with_raw_response.complete_all(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start(self, client: HiddenLayer) -> None:
        upload = client.scans.upload.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
        )
        assert_matches_type(UploadStartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: HiddenLayer) -> None:
        upload = client.scans.upload.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
            location_alias="location_alias",
            origin="Hugging Face",
            request_source="Hybrid Upload",
        )
        assert_matches_type(UploadStartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: HiddenLayer) -> None:
        response = client.scans.upload.with_raw_response.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadStartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: HiddenLayer) -> None:
        with client.scans.upload.with_streaming_response.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadStartResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUpload:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete_all(self, async_client: AsyncHiddenLayer) -> None:
        upload = await async_client.scans.upload.complete_all(
            "00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(UploadCompleteAllResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete_all(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.upload.with_raw_response.complete_all(
            "00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadCompleteAllResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete_all(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.upload.with_streaming_response.complete_all(
            "00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadCompleteAllResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_complete_all(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.upload.with_raw_response.complete_all(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncHiddenLayer) -> None:
        upload = await async_client.scans.upload.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
        )
        assert_matches_type(UploadStartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        upload = await async_client.scans.upload.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
            location_alias="location_alias",
            origin="Hugging Face",
            request_source="Hybrid Upload",
        )
        assert_matches_type(UploadStartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.upload.with_raw_response.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadStartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.upload.with_streaming_response.start(
            model_name="model_name",
            model_version="model_version",
            requesting_entity="requesting_entity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadStartResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True
