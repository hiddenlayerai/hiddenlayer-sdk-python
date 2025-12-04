# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types.scans.upload import FileAddResponse, FileCompleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: HiddenLayer) -> None:
        file = client.scans.upload.file.add(
            scan_id="00000000-0000-0000-0000-000000000000",
            file_content_length=12345,
            file_name="exampleFile.txt",
        )
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: HiddenLayer) -> None:
        response = client.scans.upload.file.with_raw_response.add(
            scan_id="00000000-0000-0000-0000-000000000000",
            file_content_length=12345,
            file_name="exampleFile.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: HiddenLayer) -> None:
        with client.scans.upload.file.with_streaming_response.add(
            scan_id="00000000-0000-0000-0000-000000000000",
            file_content_length=12345,
            file_name="exampleFile.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileAddResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.upload.file.with_raw_response.add(
                scan_id="",
                file_content_length=12345,
                file_name="exampleFile.txt",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete(self, client: HiddenLayer) -> None:
        file = client.scans.upload.file.complete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(FileCompleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: HiddenLayer) -> None:
        response = client.scans.upload.file.with_raw_response.complete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCompleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: HiddenLayer) -> None:
        with client.scans.upload.file.with_streaming_response.complete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCompleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.upload.file.with_raw_response.complete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                scan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.scans.upload.file.with_raw_response.complete(
                file_id="",
                scan_id="00000000-0000-0000-0000-000000000000",
            )


class TestAsyncFile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncHiddenLayer) -> None:
        file = await async_client.scans.upload.file.add(
            scan_id="00000000-0000-0000-0000-000000000000",
            file_content_length=12345,
            file_name="exampleFile.txt",
        )
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.upload.file.with_raw_response.add(
            scan_id="00000000-0000-0000-0000-000000000000",
            file_content_length=12345,
            file_name="exampleFile.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.upload.file.with_streaming_response.add(
            scan_id="00000000-0000-0000-0000-000000000000",
            file_content_length=12345,
            file_name="exampleFile.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileAddResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.upload.file.with_raw_response.add(
                scan_id="",
                file_content_length=12345,
                file_name="exampleFile.txt",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncHiddenLayer) -> None:
        file = await async_client.scans.upload.file.complete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(FileCompleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.upload.file.with_raw_response.complete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCompleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.upload.file.with_streaming_response.complete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCompleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.upload.file.with_raw_response.complete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                scan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.scans.upload.file.with_raw_response.complete(
                file_id="",
                scan_id="00000000-0000-0000-0000-000000000000",
            )
