# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types.model_intel import FileRetrieveResponse, FileGetMetadataResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: HiddenLayer) -> None:
        file = client.model_intel.files.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HiddenLayer) -> None:
        file = client.model_intel.files.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            cursor="cursor",
            page_size=50,
        )
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: HiddenLayer) -> None:
        response = client.model_intel.files.with_raw_response.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: HiddenLayer) -> None:
        with client.model_intel.files.with_streaming_response.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRetrieveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sha256` but received ''"):
            client.model_intel.files.with_raw_response.retrieve(
                sha256="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_metadata(self, client: HiddenLayer) -> None:
        file = client.model_intel.files.get_metadata(
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        assert_matches_type(FileGetMetadataResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_metadata(self, client: HiddenLayer) -> None:
        response = client.model_intel.files.with_raw_response.get_metadata(
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileGetMetadataResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_metadata(self, client: HiddenLayer) -> None:
        with client.model_intel.files.with_streaming_response.get_metadata(
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileGetMetadataResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_metadata(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sha256` but received ''"):
            client.model_intel.files.with_raw_response.get_metadata(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        file = await async_client.model_intel.files.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        file = await async_client.model_intel.files.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            cursor="cursor",
            page_size=50,
        )
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.model_intel.files.with_raw_response.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.model_intel.files.with_streaming_response.retrieve(
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRetrieveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sha256` but received ''"):
            await async_client.model_intel.files.with_raw_response.retrieve(
                sha256="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_metadata(self, async_client: AsyncHiddenLayer) -> None:
        file = await async_client.model_intel.files.get_metadata(
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        assert_matches_type(FileGetMetadataResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_metadata(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.model_intel.files.with_raw_response.get_metadata(
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileGetMetadataResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_metadata(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.model_intel.files.with_streaming_response.get_metadata(
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileGetMetadataResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_metadata(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sha256` but received ''"):
            await async_client.model_intel.files.with_raw_response.get_metadata(
                "",
            )
