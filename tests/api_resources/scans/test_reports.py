# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: HiddenLayer) -> None:
        report = client.scans.reports.create(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )
        assert report is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: HiddenLayer) -> None:
        response = client.scans.reports.with_raw_response.create(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert report is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: HiddenLayer) -> None:
        with client.scans.reports.with_streaming_response.create(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.scans.reports.with_raw_response.create(
                scan_id="",
                location="location",
            )


class TestAsyncReports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncHiddenLayer) -> None:
        report = await async_client.scans.reports.create(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )
        assert report is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.scans.reports.with_raw_response.create(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert report is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.scans.reports.with_streaming_response.create(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location="location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.scans.reports.with_raw_response.create(
                scan_id="",
                location="location",
            )
