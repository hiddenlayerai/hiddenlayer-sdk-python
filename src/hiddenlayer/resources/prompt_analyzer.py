# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import prompt_analyzer_create_params
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
from ..types.prompt_analyzer_create_response import PromptAnalyzerCreateResponse

__all__ = ["PromptAnalyzerResource", "AsyncPromptAnalyzerResource"]


class PromptAnalyzerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptAnalyzerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PromptAnalyzerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptAnalyzerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return PromptAnalyzerResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        model: str | Omit = omit,
        output: str | Omit = omit,
        hl_project_id: str | Omit = omit,
        x_requester_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAnalyzerCreateResponse:
        """
        Analyze LLM Prompt and Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "X-Requester-Id": x_requester_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/api/v1/submit/prompt-analyzer",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "model": model,
                    "output": output,
                },
                prompt_analyzer_create_params.PromptAnalyzerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAnalyzerCreateResponse,
        )


class AsyncPromptAnalyzerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptAnalyzerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptAnalyzerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptAnalyzerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncPromptAnalyzerResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        model: str | Omit = omit,
        output: str | Omit = omit,
        hl_project_id: str | Omit = omit,
        x_requester_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAnalyzerCreateResponse:
        """
        Analyze LLM Prompt and Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "X-Requester-Id": x_requester_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/api/v1/submit/prompt-analyzer",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "model": model,
                    "output": output,
                },
                prompt_analyzer_create_params.PromptAnalyzerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAnalyzerCreateResponse,
        )


class PromptAnalyzerResourceWithRawResponse:
    def __init__(self, prompt_analyzer: PromptAnalyzerResource) -> None:
        self._prompt_analyzer = prompt_analyzer

        self.create = to_raw_response_wrapper(
            prompt_analyzer.create,
        )


class AsyncPromptAnalyzerResourceWithRawResponse:
    def __init__(self, prompt_analyzer: AsyncPromptAnalyzerResource) -> None:
        self._prompt_analyzer = prompt_analyzer

        self.create = async_to_raw_response_wrapper(
            prompt_analyzer.create,
        )


class PromptAnalyzerResourceWithStreamingResponse:
    def __init__(self, prompt_analyzer: PromptAnalyzerResource) -> None:
        self._prompt_analyzer = prompt_analyzer

        self.create = to_streamed_response_wrapper(
            prompt_analyzer.create,
        )


class AsyncPromptAnalyzerResourceWithStreamingResponse:
    def __init__(self, prompt_analyzer: AsyncPromptAnalyzerResource) -> None:
        self._prompt_analyzer = prompt_analyzer

        self.create = async_to_streamed_response_wrapper(
            prompt_analyzer.create,
        )
