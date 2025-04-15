# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_health(self, client: HiddenLayer) -> None:
        scan = client.scans.check_health()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_health(self, client: HiddenLayer) -> None:
        response = client.scans.with_raw_response.check_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_health(self, client: HiddenLayer) -> None:
        with client.scans.with_streaming_response.check_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert scan is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_check_readiness(self, client: HiddenLayer) -> None:
        scan = client.scans.check_readiness()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_readiness(self, client: HiddenLayer) -> None:
        response = client.scans.with_raw_response.check_readiness()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_readiness(self, client: HiddenLayer) -> None:
        with client.scans.with_streaming_response.check_readiness() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert scan is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_report(self, client: HiddenLayer) -> None:
        scan = client.scans.create_report(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_report(self, client: HiddenLayer) -> None:
        response = client.scans.with_raw_response.create_report(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_report(self, client: HiddenLayer) -> None:
        with client.scans.with_streaming_response.create_report(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert scan is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_report(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.with_raw_response.create_report(
                scan_id="",
                location="location",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_results(self, client: HiddenLayer) -> None:
        scan = client.scans.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, scan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_results_with_all_params(self, client: HiddenLayer) -> None:
        scan = client.scans.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(object, scan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_results(self, client: HiddenLayer) -> None:
        response = client.scans.with_raw_response.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(object, scan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_results(self, client: HiddenLayer) -> None:
        with client.scans.with_streaming_response.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(object, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_results(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.with_raw_response.retrieve_results(
                scan_id="",
            )


class TestAsyncScans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_health(self, async_client: AsyncHiddenLayer) -> None:
        scan = await async_client.scans.check_health()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_health(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.with_raw_response.check_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_health(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.with_streaming_response.check_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert scan is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_readiness(self, async_client: AsyncHiddenLayer) -> None:
        scan = await async_client.scans.check_readiness()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_readiness(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.with_raw_response.check_readiness()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_readiness(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.with_streaming_response.check_readiness() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert scan is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_report(self, async_client: AsyncHiddenLayer) -> None:
        scan = await async_client.scans.create_report(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_report(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.with_raw_response.create_report(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert scan is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_report(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.with_streaming_response.create_report(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert scan is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_report(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.with_raw_response.create_report(
                scan_id="",
                location="location",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_results(self, async_client: AsyncHiddenLayer) -> None:
        scan = await async_client.scans.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, scan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_results_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        scan = await async_client.scans.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(object, scan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_results(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.with_raw_response.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(object, scan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_results(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.with_streaming_response.retrieve_results(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(object, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_results(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.with_raw_response.retrieve_results(
                scan_id="",
            )
