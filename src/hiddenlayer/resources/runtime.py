# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import (
    runtime_evaluate_request_params,
    runtime_evaluate_response_params,
    runtime_evaluate_interaction_params,
)
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
from ..types.runtime_evaluate_request_response import RuntimeEvaluateRequestResponse
from ..types.runtime_evaluate_response_response import RuntimeEvaluateResponseResponse
from ..types.runtime_evaluate_interaction_response import RuntimeEvaluateInteractionResponse

__all__ = ["RuntimeResource", "AsyncRuntimeResource"]


class RuntimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RuntimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RuntimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RuntimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return RuntimeResourceWithStreamingResponse(self)

    def evaluate_interaction(
        self,
        *,
        interaction: runtime_evaluate_interaction_params.Interaction,
        metadata: runtime_evaluate_interaction_params.Metadata,
        hl_project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuntimeEvaluateInteractionResponse:
        """Performs synchronous security evaluation on an LLM **interaction**.

        The
        interaction can be a standalone user prompt, a standalone model response, a
        partial exchange, or a long multi-turn message history. The endpoint imposes no
        requirement that the messages form a complete request/response pair.

        The request carries `metadata` and an `interaction` payload. The `interaction`
        field accepts either:

        - the **canonical**, provider-agnostic form (`CanonicalInteraction`) — an
          ordered sequence of messages (user, assistant, system, tool) with their role
          and content parts, and optionally the tool catalog that was in scope; or
        - a **native LLM-provider payload** passed through verbatim. Supported provider
          formats:
          - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
          - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
          - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

        Returns the evaluation context (`evaluated_interaction`): the canonicalized
        messages with per-message signals and findings attached. Also returns the policy
        outcome, which carries the enforcement action, threat level, any detections, and
        the effective payload the caller should forward
        (`outcome.effective_interaction`).

        Use this endpoint when you need full evaluation results. For inline pass-through
        (provider request/response payloads returned in the same provider format), use
        the request-evaluations and response-evaluations endpoints instead.

        Args:
          interaction: The interaction to evaluate. Accepts either the canonical form
              (`CanonicalInteraction` — `messages` and optional `tools_available`) or a native
              LLM-provider payload passed through verbatim. Supported provider formats are
              OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages.
              `ProviderPayload` is intentionally permissive (any JSON object) so callers can
              supply provider-native shapes without schema constraints.

          metadata: Metadata about the LLM interactions being evaluated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"HL-Project-Id": hl_project_id}), **(extra_headers or {})}
        return self._post(
            "/detection/v2/interaction-evaluations",
            body=maybe_transform(
                {
                    "interaction": interaction,
                    "metadata": metadata,
                },
                runtime_evaluate_interaction_params.RuntimeEvaluateInteractionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeEvaluateInteractionResponse,
        )

    def evaluate_request(
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
    ) -> RuntimeEvaluateRequestResponse:
        """
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
            body=maybe_transform(body, runtime_evaluate_request_params.RuntimeEvaluateRequestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeEvaluateRequestResponse,
        )

    def evaluate_response(
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
    ) -> RuntimeEvaluateResponseResponse:
        """
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
            body=maybe_transform(body, runtime_evaluate_response_params.RuntimeEvaluateResponseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeEvaluateResponseResponse,
        )


class AsyncRuntimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRuntimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRuntimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRuntimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncRuntimeResourceWithStreamingResponse(self)

    async def evaluate_interaction(
        self,
        *,
        interaction: runtime_evaluate_interaction_params.Interaction,
        metadata: runtime_evaluate_interaction_params.Metadata,
        hl_project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuntimeEvaluateInteractionResponse:
        """Performs synchronous security evaluation on an LLM **interaction**.

        The
        interaction can be a standalone user prompt, a standalone model response, a
        partial exchange, or a long multi-turn message history. The endpoint imposes no
        requirement that the messages form a complete request/response pair.

        The request carries `metadata` and an `interaction` payload. The `interaction`
        field accepts either:

        - the **canonical**, provider-agnostic form (`CanonicalInteraction`) — an
          ordered sequence of messages (user, assistant, system, tool) with their role
          and content parts, and optionally the tool catalog that was in scope; or
        - a **native LLM-provider payload** passed through verbatim. Supported provider
          formats:
          - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
          - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
          - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

        Returns the evaluation context (`evaluated_interaction`): the canonicalized
        messages with per-message signals and findings attached. Also returns the policy
        outcome, which carries the enforcement action, threat level, any detections, and
        the effective payload the caller should forward
        (`outcome.effective_interaction`).

        Use this endpoint when you need full evaluation results. For inline pass-through
        (provider request/response payloads returned in the same provider format), use
        the request-evaluations and response-evaluations endpoints instead.

        Args:
          interaction: The interaction to evaluate. Accepts either the canonical form
              (`CanonicalInteraction` — `messages` and optional `tools_available`) or a native
              LLM-provider payload passed through verbatim. Supported provider formats are
              OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages.
              `ProviderPayload` is intentionally permissive (any JSON object) so callers can
              supply provider-native shapes without schema constraints.

          metadata: Metadata about the LLM interactions being evaluated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"HL-Project-Id": hl_project_id}), **(extra_headers or {})}
        return await self._post(
            "/detection/v2/interaction-evaluations",
            body=await async_maybe_transform(
                {
                    "interaction": interaction,
                    "metadata": metadata,
                },
                runtime_evaluate_interaction_params.RuntimeEvaluateInteractionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeEvaluateInteractionResponse,
        )

    async def evaluate_request(
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
    ) -> RuntimeEvaluateRequestResponse:
        """
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
            body=await async_maybe_transform(body, runtime_evaluate_request_params.RuntimeEvaluateRequestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeEvaluateRequestResponse,
        )

    async def evaluate_response(
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
    ) -> RuntimeEvaluateResponseResponse:
        """
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
            body=await async_maybe_transform(body, runtime_evaluate_response_params.RuntimeEvaluateResponseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeEvaluateResponseResponse,
        )


class RuntimeResourceWithRawResponse:
    def __init__(self, runtime: RuntimeResource) -> None:
        self._runtime = runtime

        self.evaluate_interaction = to_raw_response_wrapper(
            runtime.evaluate_interaction,
        )
        self.evaluate_request = to_raw_response_wrapper(
            runtime.evaluate_request,
        )
        self.evaluate_response = to_raw_response_wrapper(
            runtime.evaluate_response,
        )


class AsyncRuntimeResourceWithRawResponse:
    def __init__(self, runtime: AsyncRuntimeResource) -> None:
        self._runtime = runtime

        self.evaluate_interaction = async_to_raw_response_wrapper(
            runtime.evaluate_interaction,
        )
        self.evaluate_request = async_to_raw_response_wrapper(
            runtime.evaluate_request,
        )
        self.evaluate_response = async_to_raw_response_wrapper(
            runtime.evaluate_response,
        )


class RuntimeResourceWithStreamingResponse:
    def __init__(self, runtime: RuntimeResource) -> None:
        self._runtime = runtime

        self.evaluate_interaction = to_streamed_response_wrapper(
            runtime.evaluate_interaction,
        )
        self.evaluate_request = to_streamed_response_wrapper(
            runtime.evaluate_request,
        )
        self.evaluate_response = to_streamed_response_wrapper(
            runtime.evaluate_response,
        )


class AsyncRuntimeResourceWithStreamingResponse:
    def __init__(self, runtime: AsyncRuntimeResource) -> None:
        self._runtime = runtime

        self.evaluate_interaction = async_to_streamed_response_wrapper(
            runtime.evaluate_interaction,
        )
        self.evaluate_request = async_to_streamed_response_wrapper(
            runtime.evaluate_request,
        )
        self.evaluate_response = async_to_streamed_response_wrapper(
            runtime.evaluate_response,
        )
