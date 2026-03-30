# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import interaction_analyze_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.interaction_analyze_response import InteractionAnalyzeResponse

__all__ = ["InteractionsResource", "AsyncInteractionsResource"]


class InteractionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return InteractionsResourceWithStreamingResponse(self)

    def analyze(
        self,
        *,
        metadata: interaction_analyze_params.Metadata,
        input: interaction_analyze_params.Input | Omit = omit,
        output: interaction_analyze_params.Output | Omit = omit,
        hl_project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InteractionAnalyzeResponse:
        """
        Performs a detailed security analysis of the input and/or output of LLM
        interactions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"HL-Project-Id": hl_project_id}), **(extra_headers or {})}
        return self._post(
            "/detection/v1/interactions",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "input": input,
                    "output": output,
                },
                interaction_analyze_params.InteractionAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InteractionAnalyzeResponse,
        )


class AsyncInteractionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncInteractionsResourceWithStreamingResponse(self)

    async def analyze(
        self,
        *,
        metadata: interaction_analyze_params.Metadata,
        input: interaction_analyze_params.Input | Omit = omit,
        output: interaction_analyze_params.Output | Omit = omit,
        hl_project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InteractionAnalyzeResponse:
        """
        Performs a detailed security analysis of the input and/or output of LLM
        interactions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"HL-Project-Id": hl_project_id}), **(extra_headers or {})}
        return await self._post(
            "/detection/v1/interactions",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "input": input,
                    "output": output,
                },
                interaction_analyze_params.InteractionAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InteractionAnalyzeResponse,
        )


class InteractionsResourceWithRawResponse:
    def __init__(self, interactions: InteractionsResource) -> None:
        self._interactions = interactions

        self.analyze = to_raw_response_wrapper(
            interactions.analyze,
        )


class AsyncInteractionsResourceWithRawResponse:
    def __init__(self, interactions: AsyncInteractionsResource) -> None:
        self._interactions = interactions

        self.analyze = async_to_raw_response_wrapper(
            interactions.analyze,
        )


class InteractionsResourceWithStreamingResponse:
    def __init__(self, interactions: InteractionsResource) -> None:
        self._interactions = interactions

        self.analyze = to_streamed_response_wrapper(
            interactions.analyze,
        )


class AsyncInteractionsResourceWithStreamingResponse:
    def __init__(self, interactions: AsyncInteractionsResource) -> None:
        self._interactions = interactions

        self.analyze = async_to_streamed_response_wrapper(
            interactions.analyze,
        )
