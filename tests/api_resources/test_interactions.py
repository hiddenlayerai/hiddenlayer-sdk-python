# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types import InteractionAnalyzeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInteractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze(self, client: HiddenLayer) -> None:
        interaction = client.interactions.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
            },
        )
        assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_with_all_params(self, client: HiddenLayer) -> None:
        interaction = client.interactions.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
                "provider": "openai",
            },
            input={
                "messages": [
                    {
                        "content": "What the largest moon of jupiter?",
                        "role": "user",
                    }
                ]
            },
            output={
                "messages": [
                    {
                        "content": "The largest moon of Jupiter is Ganymede.",
                        "role": "assistant",
                    }
                ]
            },
            hl_project_id="internal-search-chatbot",
        )
        assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze(self, client: HiddenLayer) -> None:
        response = client.interactions.with_raw_response.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interaction = response.parse()
        assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze(self, client: HiddenLayer) -> None:
        with client.interactions.with_streaming_response.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interaction = response.parse()
            assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInteractions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze(self, async_client: AsyncHiddenLayer) -> None:
        interaction = await async_client.interactions.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
            },
        )
        assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        interaction = await async_client.interactions.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
                "provider": "openai",
            },
            input={
                "messages": [
                    {
                        "content": "What the largest moon of jupiter?",
                        "role": "user",
                    }
                ]
            },
            output={
                "messages": [
                    {
                        "content": "The largest moon of Jupiter is Ganymede.",
                        "role": "assistant",
                    }
                ]
            },
            hl_project_id="internal-search-chatbot",
        )
        assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.interactions.with_raw_response.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interaction = await response.parse()
        assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.interactions.with_streaming_response.analyze(
            metadata={
                "model": "gpt-5",
                "requester_id": "user-1234",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interaction = await response.parse()
            assert_matches_type(InteractionAnalyzeResponse, interaction, path=["response"])

        assert cast(Any, response.is_closed) is True
