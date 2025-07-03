# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer._utils import parse_datetime
from hiddenlayer.types.scans import ScanReport, ResultListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: HiddenLayer) -> None:
        result = client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            x_correlation_id="00000000-0000-0000-0000-000000000000",
            has_detections=True,
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            x_correlation_id="00000000-0000-0000-0000-000000000000",
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
            x_correlation_id="00000000-0000-0000-0000-000000000000",
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
                x_correlation_id="00000000-0000-0000-0000-000000000000",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: HiddenLayer) -> None:
        result = client.scans.results.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: HiddenLayer) -> None:
        result = client.scans.results.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
            detection_category="detection_category",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            latest_per_model_version_only=True,
            limit=1,
            model_ids=["string"],
            model_name={
                "contains": "contains",
                "eq": "eq",
            },
            model_version_ids=["string"],
            offset=0,
            scanner_version="scanner_version",
            severity=["string"],
            sort="sort",
            source={"eq": "adhoc"},
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["string"],
        )
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: HiddenLayer) -> None:
        response = client.scans.results.with_raw_response.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: HiddenLayer) -> None:
        with client.scans.results.with_streaming_response.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultListResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            x_correlation_id="00000000-0000-0000-0000-000000000000",
            has_detections=True,
        )
        assert_matches_type(ScanReport, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.retrieve(
            scan_id="00000000-0000-0000-0000-000000000000",
            x_correlation_id="00000000-0000-0000-0000-000000000000",
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
            x_correlation_id="00000000-0000-0000-0000-000000000000",
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
                x_correlation_id="00000000-0000-0000-0000-000000000000",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        )
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        result = await async_client.scans.results.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
            detection_category="detection_category",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            latest_per_model_version_only=True,
            limit=1,
            model_ids=["string"],
            model_name={
                "contains": "contains",
                "eq": "eq",
            },
            model_version_ids=["string"],
            offset=0,
            scanner_version="scanner_version",
            severity=["string"],
            sort="sort",
            source={"eq": "adhoc"},
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["string"],
        )
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.results.with_raw_response.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultListResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.results.with_streaming_response.list(
            x_correlation_id="00000000-0000-0000-0000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultListResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True
