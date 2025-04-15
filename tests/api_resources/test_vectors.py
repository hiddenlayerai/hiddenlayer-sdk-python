# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hiddenlayer_sdk import HiddenLayer, AsyncHiddenLayer
from hiddenlayer_sdk.types import VectorSubmitVectorsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_submit_vectors(self, client: HiddenLayer) -> None:
        vector = client.vectors.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
        )
        assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_submit_vectors_with_all_params(self, client: HiddenLayer) -> None:
        vector = client.vectors.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
            event_time="event_time",
            metadata={},
            predictions=[0],
            requester_id="requester_id",
            tags=["string"],
        )
        assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_submit_vectors(self, client: HiddenLayer) -> None:
        response = client.vectors.with_raw_response.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector = response.parse()
        assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_submit_vectors(self, client: HiddenLayer) -> None:
        with client.vectors.with_streaming_response.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector = response.parse()
            assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_submit_vectors(self, async_client: AsyncHiddenLayer) -> None:
        vector = await async_client.vectors.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
        )
        assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_submit_vectors_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        vector = await async_client.vectors.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
            event_time="event_time",
            metadata={},
            predictions=[0],
            requester_id="requester_id",
            tags=["string"],
        )
        assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_submit_vectors(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.vectors.with_raw_response.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector = await response.parse()
        assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_submit_vectors(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.vectors.with_streaming_response.submit_vectors(
            input_layer="input_layer",
            input_layer_dtype="input_layer_dtype",
            input_layer_shape=[0],
            output_layer="output_layer",
            output_layer_dtype="output_layer_dtype",
            output_layer_shape=[0],
            sensor_id="sensor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector = await response.parse()
            assert_matches_type(VectorSubmitVectorsResponse, vector, path=["response"])

        assert cast(Any, response.is_closed) is True
