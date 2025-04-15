# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..types import vector_submit_vectors_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.vector_submit_vectors_response import VectorSubmitVectorsResponse

__all__ = ["VectorsResource", "AsyncVectorsResource"]


class VectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#with_streaming_response
        """
        return VectorsResourceWithStreamingResponse(self)

    def submit_vectors(
        self,
        *,
        input_layer: str,
        input_layer_dtype: str,
        input_layer_shape: Iterable[float],
        output_layer: str,
        output_layer_dtype: str,
        output_layer_shape: Iterable[float],
        sensor_id: str,
        event_time: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        predictions: Iterable[float] | NotGiven = NOT_GIVEN,
        requester_id: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorSubmitVectorsResponse:
        """
        Submit vectors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/submit",
            body=maybe_transform(
                {
                    "input_layer": input_layer,
                    "input_layer_dtype": input_layer_dtype,
                    "input_layer_shape": input_layer_shape,
                    "output_layer": output_layer,
                    "output_layer_dtype": output_layer_dtype,
                    "output_layer_shape": output_layer_shape,
                    "sensor_id": sensor_id,
                    "event_time": event_time,
                    "metadata": metadata,
                    "predictions": predictions,
                    "requester_id": requester_id,
                    "tags": tags,
                },
                vector_submit_vectors_params.VectorSubmitVectorsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorSubmitVectorsResponse,
        )


class AsyncVectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncVectorsResourceWithStreamingResponse(self)

    async def submit_vectors(
        self,
        *,
        input_layer: str,
        input_layer_dtype: str,
        input_layer_shape: Iterable[float],
        output_layer: str,
        output_layer_dtype: str,
        output_layer_shape: Iterable[float],
        sensor_id: str,
        event_time: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        predictions: Iterable[float] | NotGiven = NOT_GIVEN,
        requester_id: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorSubmitVectorsResponse:
        """
        Submit vectors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/submit",
            body=await async_maybe_transform(
                {
                    "input_layer": input_layer,
                    "input_layer_dtype": input_layer_dtype,
                    "input_layer_shape": input_layer_shape,
                    "output_layer": output_layer,
                    "output_layer_dtype": output_layer_dtype,
                    "output_layer_shape": output_layer_shape,
                    "sensor_id": sensor_id,
                    "event_time": event_time,
                    "metadata": metadata,
                    "predictions": predictions,
                    "requester_id": requester_id,
                    "tags": tags,
                },
                vector_submit_vectors_params.VectorSubmitVectorsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorSubmitVectorsResponse,
        )


class VectorsResourceWithRawResponse:
    def __init__(self, vectors: VectorsResource) -> None:
        self._vectors = vectors

        self.submit_vectors = to_raw_response_wrapper(
            vectors.submit_vectors,
        )


class AsyncVectorsResourceWithRawResponse:
    def __init__(self, vectors: AsyncVectorsResource) -> None:
        self._vectors = vectors

        self.submit_vectors = async_to_raw_response_wrapper(
            vectors.submit_vectors,
        )


class VectorsResourceWithStreamingResponse:
    def __init__(self, vectors: VectorsResource) -> None:
        self._vectors = vectors

        self.submit_vectors = to_streamed_response_wrapper(
            vectors.submit_vectors,
        )


class AsyncVectorsResourceWithStreamingResponse:
    def __init__(self, vectors: AsyncVectorsResource) -> None:
        self._vectors = vectors

        self.submit_vectors = async_to_streamed_response_wrapper(
            vectors.submit_vectors,
        )
