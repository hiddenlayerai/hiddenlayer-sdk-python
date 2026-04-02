# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types import (
    RuntimeEvaluateRequestResponse,
    RuntimeEvaluateResponseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuntime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_evaluate_request(self, client: HiddenLayer) -> None:
        runtime = client.runtime.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
        )
        assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_evaluate_request_with_all_params(self, client: HiddenLayer) -> None:
        runtime = client.runtime.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
            hl_project_id="internal-search-chatbot",
            hl_runtime_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
        )
        assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_evaluate_request(self, client: HiddenLayer) -> None:
        response = client.runtime.with_raw_response.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = response.parse()
        assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_evaluate_request(self, client: HiddenLayer) -> None:
        with client.runtime.with_streaming_response.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = response.parse()
            assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_evaluate_response(self, client: HiddenLayer) -> None:
        runtime = client.runtime.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
        )
        assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_evaluate_response_with_all_params(self, client: HiddenLayer) -> None:
        runtime = client.runtime.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
            hl_project_id="internal-search-chatbot",
            hl_runtime_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
        )
        assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_evaluate_response(self, client: HiddenLayer) -> None:
        response = client.runtime.with_raw_response.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = response.parse()
        assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_evaluate_response(self, client: HiddenLayer) -> None:
        with client.runtime.with_streaming_response.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = response.parse()
            assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRuntime:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_evaluate_request(self, async_client: AsyncHiddenLayer) -> None:
        runtime = await async_client.runtime.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
        )
        assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_evaluate_request_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        runtime = await async_client.runtime.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
            hl_project_id="internal-search-chatbot",
            hl_runtime_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
        )
        assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_evaluate_request(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.runtime.with_raw_response.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = await response.parse()
        assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_evaluate_request(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.runtime.with_streaming_response.evaluate_request(
            body={
                "model": "bar",
                "messages": "bar",
                "max_tokens": "bar",
                "temperature": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = await response.parse()
            assert_matches_type(RuntimeEvaluateRequestResponse, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_evaluate_response(self, async_client: AsyncHiddenLayer) -> None:
        runtime = await async_client.runtime.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
        )
        assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_evaluate_response_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        runtime = await async_client.runtime.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
            hl_project_id="internal-search-chatbot",
            hl_runtime_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
        )
        assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_evaluate_response(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.runtime.with_raw_response.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = await response.parse()
        assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_evaluate_response(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.runtime.with_streaming_response.evaluate_response(
            body={
                "id": "bar",
                "object": "bar",
                "created": "bar",
                "model": "bar",
                "choices": "bar",
                "usage": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = await response.parse()
            assert_matches_type(RuntimeEvaluateResponseResponse, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True
