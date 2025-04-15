# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types.models import CardListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: HiddenLayer) -> None:
        card = client.models.cards.list()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: HiddenLayer) -> None:
        card = client.models.cards.list(
            limit=1,
            model_name_contains="model_name[contains]",
            model_name_eq="model_name[eq]",
            offset=0,
            sort="sort",
        )
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: HiddenLayer) -> None:
        response = client.models.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: HiddenLayer) -> None:
        with client.models.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncHiddenLayer) -> None:
        card = await async_client.models.cards.list()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        card = await async_client.models.cards.list(
            limit=1,
            model_name_contains="model_name[contains]",
            model_name_eq="model_name[eq]",
            offset=0,
            sort="sort",
        )
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.models.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.models.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True
