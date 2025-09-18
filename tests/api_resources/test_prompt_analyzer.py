# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types import PromptAnalyzerCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptAnalyzer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HiddenLayer) -> None:
        prompt_analyzer = client.prompt_analyzer.create(
            prompt="Hello World",
        )
        assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HiddenLayer) -> None:
        prompt_analyzer = client.prompt_analyzer.create(
            prompt="Hello World",
            model="mistral-tiny",
            output="Hello, how can I help you today?",
            hl_project_id="internal-search-chatbot",
            x_requester_id="X-Requester-Id",
        )
        assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HiddenLayer) -> None:
        response = client.prompt_analyzer.with_raw_response.create(
            prompt="Hello World",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_analyzer = response.parse()
        assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HiddenLayer) -> None:
        with client.prompt_analyzer.with_streaming_response.create(
            prompt="Hello World",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_analyzer = response.parse()
            assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPromptAnalyzer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHiddenLayer) -> None:
        prompt_analyzer = await async_client.prompt_analyzer.create(
            prompt="Hello World",
        )
        assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        prompt_analyzer = await async_client.prompt_analyzer.create(
            prompt="Hello World",
            model="mistral-tiny",
            output="Hello, how can I help you today?",
            hl_project_id="internal-search-chatbot",
            x_requester_id="X-Requester-Id",
        )
        assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.prompt_analyzer.with_raw_response.create(
            prompt="Hello World",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_analyzer = await response.parse()
        assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.prompt_analyzer.with_streaming_response.create(
            prompt="Hello World",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_analyzer = await response.parse()
            assert_matches_type(PromptAnalyzerCreateResponse, prompt_analyzer, path=["response"])

        assert cast(Any, response.is_closed) is True
