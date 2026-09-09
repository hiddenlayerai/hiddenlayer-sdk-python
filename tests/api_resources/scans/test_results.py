# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.pagination import SyncCursorPagination, AsyncCursorPagination
from hiddenlayer.types.scans import ScanFileResult, ScanReportSummary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files(self, client: HiddenLayer) -> None:
        result = client.scans.results.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(SyncCursorPagination[ScanFileResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
            cursor="cursor",
            has_detections=True,
            page_size=50,
        )
        assert_matches_type(SyncCursorPagination[ScanFileResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_files(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(SyncCursorPagination[ScanFileResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_files(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(SyncCursorPagination[ScanFileResult], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_files(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.results.with_raw_response.list_files(
                scan_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_summary(self, client: HiddenLayer) -> None:
        result = client.scans.results.retrieve_summary(
            "00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReportSummary, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_summary(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.retrieve_summary(
            "00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ScanReportSummary, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.retrieve_summary(
            "00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ScanReportSummary, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_summary(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.results.with_raw_response.retrieve_summary(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sarif(self, client: HiddenLayer) -> None:
        result = client.scans.results.sarif(
            "00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(str, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sarif(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.sarif(
            "00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(str, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sarif(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.sarif(
            "00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(str, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sarif(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.results.with_raw_response.sarif(
                "",
            )


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(AsyncCursorPagination[ScanFileResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
            cursor="cursor",
            has_detections=True,
            page_size=50,
        )
        assert_matches_type(AsyncCursorPagination[ScanFileResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(AsyncCursorPagination[ScanFileResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.list_files(
            scan_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(AsyncCursorPagination[ScanFileResult], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_files(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.results.with_raw_response.list_files(
                scan_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.retrieve_summary(
            "00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReportSummary, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.retrieve_summary(
            "00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ScanReportSummary, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.retrieve_summary(
            "00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ScanReportSummary, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_summary(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.results.with_raw_response.retrieve_summary(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sarif(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.sarif(
            "00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(str, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sarif(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.sarif(
            "00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(str, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sarif(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.sarif(
            "00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(str, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sarif(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.results.with_raw_response.sarif(
                "",
            )
