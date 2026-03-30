# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import detection_request_evaluation_params, detection_response_evaluation_params
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
from ..types.detection_request_evaluation_response import DetectionRequestEvaluationResponse
from ..types.detection_response_evaluation_response import DetectionResponseEvaluationResponse
from ..lib._beta import warn_beta

__all__ = ["DetectionResource", "AsyncDetectionResource"]


class DetectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return DetectionResourceWithStreamingResponse(self)

    def request_evaluation(
        self,
        *,
        body: Dict[str, object],
        hl_project_id: str | Omit = omit,
        hl_runtime_session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetectionRequestEvaluationResponse:
        """
        [BETA] This endpoint is not GA or Production ready and is subject to changes at
        any time. Breaking changes may occur.

        Analyzes an LLM request payload for security threats before it is sent to the
        model.

        Accepts any valid provider request payload and returns:

        - If detect or redact action: the request payload (potentially modified) in the
          provider's request format
        - If block action: a canned block message in the provider's response format

        Use this endpoint inline in your LLM pipeline to evaluate prompts before they
        reach the model.

        Supported provider formats:

        - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
        - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
        - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

        Args:
          body: A pass-through payload in the native format of the LLM provider. Any valid
              provider request or response payload is accepted as-is and returned in the same
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        warn_beta("DetectionResource.request_evaluation")
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "HL-Runtime-Session-Id": hl_runtime_session_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/detection/v2/request-evaluations",
            body=maybe_transform(body, detection_request_evaluation_params.DetectionRequestEvaluationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetectionRequestEvaluationResponse,
        )

    def response_evaluation(
        self,
        *,
        body: Dict[str, object],
        hl_project_id: str | Omit = omit,
        hl_runtime_session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetectionResponseEvaluationResponse:
        """
        [BETA] This endpoint is not GA or Production ready and is subject to changes at
        any time. Breaking changes may occur.

        Analyzes an LLM response payload for security threats after it is received from
        the model.

        Accepts any valid provider response payload and returns:

        - If detect or redact action: the response payload (potentially modified) in the
          provider's response format
        - If block action: a canned block message in the provider's response format

        Use this endpoint inline in your LLM pipeline to evaluate model outputs before
        returning them to users.

        Supported provider formats:

        - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
        - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
        - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

        Args:
          body: A pass-through payload in the native format of the LLM provider. Any valid
              provider request or response payload is accepted as-is and returned in the same
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        warn_beta("DetectionResource.response_evaluation")
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "HL-Runtime-Session-Id": hl_runtime_session_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/detection/v2/response-evaluations",
            body=maybe_transform(body, detection_response_evaluation_params.DetectionResponseEvaluationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetectionResponseEvaluationResponse,
        )


class AsyncDetectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncDetectionResourceWithStreamingResponse(self)

    async def request_evaluation(
        self,
        *,
        body: Dict[str, object],
        hl_project_id: str | Omit = omit,
        hl_runtime_session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetectionRequestEvaluationResponse:
        """
        [BETA] This endpoint is not GA or Production ready and is subject to changes at
        any time. Breaking changes may occur.

        Analyzes an LLM request payload for security threats before it is sent to the
        model.

        Accepts any valid provider request payload and returns:

        - If detect or redact action: the request payload (potentially modified) in the
          provider's request format
        - If block action: a canned block message in the provider's response format

        Use this endpoint inline in your LLM pipeline to evaluate prompts before they
        reach the model.

        Supported provider formats:

        - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
        - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
        - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

        Args:
          body: A pass-through payload in the native format of the LLM provider. Any valid
              provider request or response payload is accepted as-is and returned in the same
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
     warn_beta("AsyncDetectionResource.request_evaluation")
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "HL-Runtime-Session-Id": hl_runtime_session_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/detection/v2/request-evaluations",
            body=await async_maybe_transform(
                body, detection_request_evaluation_params.DetectionRequestEvaluationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetectionRequestEvaluationResponse,
        )

    async def response_evaluation(
        self,
        *,
        body: Dict[str, object],
        hl_project_id: str | Omit = omit,
        hl_runtime_session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetectionResponseEvaluationResponse:
        """
        [BETA] This endpoint is not GA or Production ready and is subject to changes at
        any time. Breaking changes may occur.

        Analyzes an LLM response payload for security threats after it is received from
        the model.

        Accepts any valid provider response payload and returns:

        - If detect or redact action: the response payload (potentially modified) in the
          provider's response format
        - If block action: a canned block message in the provider's response format

        Use this endpoint inline in your LLM pipeline to evaluate model outputs before
        returning them to users.

        Supported provider formats:

        - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
        - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
        - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

        Args:
          body: A pass-through payload in the native format of the LLM provider. Any valid
              provider request or response payload is accepted as-is and returned in the same
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
     warn_beta("AsyncDetectionResource.response_evaluation")
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "HL-Runtime-Session-Id": hl_runtime_session_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/detection/v2/response-evaluations",
            body=await async_maybe_transform(
                body, detection_response_evaluation_params.DetectionResponseEvaluationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetectionResponseEvaluationResponse,
        )


class DetectionResourceWithRawResponse:
    def __init__(self, detection: DetectionResource) -> None:
        self._detection = detection

        self.request_evaluation = to_raw_response_wrapper(
            detection.request_evaluation,
        )
        self.response_evaluation = to_raw_response_wrapper(
            detection.response_evaluation,
        )


class AsyncDetectionResourceWithRawResponse:
    def __init__(self, detection: AsyncDetectionResource) -> None:
        self._detection = detection

        self.request_evaluation = async_to_raw_response_wrapper(
            detection.request_evaluation,
        )
        self.response_evaluation = async_to_raw_response_wrapper(
            detection.response_evaluation,
        )


class DetectionResourceWithStreamingResponse:
    def __init__(self, detection: DetectionResource) -> None:
        self._detection = detection

        self.request_evaluation = to_streamed_response_wrapper(
            detection.request_evaluation,
        )
        self.response_evaluation = to_streamed_response_wrapper(
            detection.response_evaluation,
        )


class AsyncDetectionResourceWithStreamingResponse:
    def __init__(self, detection: AsyncDetectionResource) -> None:
        self._detection = detection

        self.request_evaluation = async_to_streamed_response_wrapper(
            detection.request_evaluation,
        )
        self.response_evaluation = async_to_streamed_response_wrapper(
            detection.response_evaluation,
        )
