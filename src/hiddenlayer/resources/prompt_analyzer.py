# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import prompt_analyzer_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
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

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PromptAnalyzerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptAnalyzerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#with_streaming_response
        """
        return PromptAnalyzerResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        model: str | NotGiven = NOT_GIVEN,
        output: str | NotGiven = NOT_GIVEN,
        hl_project_id: str | NotGiven = NOT_GIVEN,
        x_llm_block_guardrail_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_input_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_input_dos_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_input_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_block_output_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_output_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_block_prompt_injection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_unsafe: bool | NotGiven = NOT_GIVEN,
        x_llm_block_unsafe_input: bool | NotGiven = NOT_GIVEN,
        x_llm_block_unsafe_output: bool | NotGiven = NOT_GIVEN,
        x_llm_entity_type: Literal["strict", "all"] | NotGiven = NOT_GIVEN,
        x_llm_input_dos_detection_threshold: str | NotGiven = NOT_GIVEN,
        x_llm_prompt_injection_scan_type: Literal["quick", "full"] | NotGiven = NOT_GIVEN,
        x_llm_redact_input_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_redact_output_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_redact_type: Literal["entity", "strict"] | NotGiven = NOT_GIVEN,
        x_llm_skip_guardrail_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_dos_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_pii_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_url_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_output_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_output_pii_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_output_url_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_prompt_injection_detection: bool | NotGiven = NOT_GIVEN,
        x_requester_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptAnalyzerCreateResponse:
        """
        Analyze LLM Prompt and Response

        Args:
          x_llm_entity_type: The type of entity to redact

          x_llm_prompt_injection_scan_type: The type of prompt injection scan to use

          x_llm_redact_type: The type of redaction to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "X-LLM-Block-Guardrail-Detection": ("true" if x_llm_block_guardrail_detection else "false")
                    if is_given(x_llm_block_guardrail_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Input-Code-Detection": ("true" if x_llm_block_input_code_detection else "false")
                    if is_given(x_llm_block_input_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Input-DOS-Detection": ("true" if x_llm_block_input_dos_detection else "false")
                    if is_given(x_llm_block_input_dos_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Input-PII": ("true" if x_llm_block_input_pii else "false")
                    if is_given(x_llm_block_input_pii)
                    else NOT_GIVEN,
                    "X-LLM-Block-Output-Code-Detection": ("true" if x_llm_block_output_code_detection else "false")
                    if is_given(x_llm_block_output_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Output-PII": ("true" if x_llm_block_output_pii else "false")
                    if is_given(x_llm_block_output_pii)
                    else NOT_GIVEN,
                    "X-LLM-Block-Prompt-Injection": ("true" if x_llm_block_prompt_injection else "false")
                    if is_given(x_llm_block_prompt_injection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Unsafe": ("true" if x_llm_block_unsafe else "false")
                    if is_given(x_llm_block_unsafe)
                    else NOT_GIVEN,
                    "X-LLM-Block-Unsafe-Input": ("true" if x_llm_block_unsafe_input else "false")
                    if is_given(x_llm_block_unsafe_input)
                    else NOT_GIVEN,
                    "X-LLM-Block-Unsafe-Output": ("true" if x_llm_block_unsafe_output else "false")
                    if is_given(x_llm_block_unsafe_output)
                    else NOT_GIVEN,
                    "X-LLM-Entity-Type": str(x_llm_entity_type) if is_given(x_llm_entity_type) else NOT_GIVEN,
                    "X-LLM-Input-DOS-Detection-Threshold": x_llm_input_dos_detection_threshold,
                    "X-LLM-Prompt-Injection-Scan-Type": str(x_llm_prompt_injection_scan_type)
                    if is_given(x_llm_prompt_injection_scan_type)
                    else NOT_GIVEN,
                    "X-LLM-Redact-Input-PII": ("true" if x_llm_redact_input_pii else "false")
                    if is_given(x_llm_redact_input_pii)
                    else NOT_GIVEN,
                    "X-LLM-Redact-Output-PII": ("true" if x_llm_redact_output_pii else "false")
                    if is_given(x_llm_redact_output_pii)
                    else NOT_GIVEN,
                    "X-LLM-Redact-Type": str(x_llm_redact_type) if is_given(x_llm_redact_type) else NOT_GIVEN,
                    "X-LLM-Skip-Guardrail-Detection": ("true" if x_llm_skip_guardrail_detection else "false")
                    if is_given(x_llm_skip_guardrail_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-Code-Detection": ("true" if x_llm_skip_input_code_detection else "false")
                    if is_given(x_llm_skip_input_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-DOS-Detection": ("true" if x_llm_skip_input_dos_detection else "false")
                    if is_given(x_llm_skip_input_dos_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-PII-Detection": ("true" if x_llm_skip_input_pii_detection else "false")
                    if is_given(x_llm_skip_input_pii_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-URL-Detection": ("true" if x_llm_skip_input_url_detection else "false")
                    if is_given(x_llm_skip_input_url_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Output-Code-Detection": ("true" if x_llm_skip_output_code_detection else "false")
                    if is_given(x_llm_skip_output_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Output-PII-Detection": ("true" if x_llm_skip_output_pii_detection else "false")
                    if is_given(x_llm_skip_output_pii_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Output-URL-Detection": ("true" if x_llm_skip_output_url_detection else "false")
                    if is_given(x_llm_skip_output_url_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Prompt-Injection-Detection": (
                        "true" if x_llm_skip_prompt_injection_detection else "false"
                    )
                    if is_given(x_llm_skip_prompt_injection_detection)
                    else NOT_GIVEN,
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

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptAnalyzerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptAnalyzerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncPromptAnalyzerResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        model: str | NotGiven = NOT_GIVEN,
        output: str | NotGiven = NOT_GIVEN,
        hl_project_id: str | NotGiven = NOT_GIVEN,
        x_llm_block_guardrail_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_input_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_input_dos_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_input_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_block_output_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_output_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_block_prompt_injection: bool | NotGiven = NOT_GIVEN,
        x_llm_block_unsafe: bool | NotGiven = NOT_GIVEN,
        x_llm_block_unsafe_input: bool | NotGiven = NOT_GIVEN,
        x_llm_block_unsafe_output: bool | NotGiven = NOT_GIVEN,
        x_llm_entity_type: Literal["strict", "all"] | NotGiven = NOT_GIVEN,
        x_llm_input_dos_detection_threshold: str | NotGiven = NOT_GIVEN,
        x_llm_prompt_injection_scan_type: Literal["quick", "full"] | NotGiven = NOT_GIVEN,
        x_llm_redact_input_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_redact_output_pii: bool | NotGiven = NOT_GIVEN,
        x_llm_redact_type: Literal["entity", "strict"] | NotGiven = NOT_GIVEN,
        x_llm_skip_guardrail_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_dos_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_pii_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_input_url_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_output_code_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_output_pii_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_output_url_detection: bool | NotGiven = NOT_GIVEN,
        x_llm_skip_prompt_injection_detection: bool | NotGiven = NOT_GIVEN,
        x_requester_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptAnalyzerCreateResponse:
        """
        Analyze LLM Prompt and Response

        Args:
          x_llm_entity_type: The type of entity to redact

          x_llm_prompt_injection_scan_type: The type of prompt injection scan to use

          x_llm_redact_type: The type of redaction to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "HL-Project-Id": hl_project_id,
                    "X-LLM-Block-Guardrail-Detection": ("true" if x_llm_block_guardrail_detection else "false")
                    if is_given(x_llm_block_guardrail_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Input-Code-Detection": ("true" if x_llm_block_input_code_detection else "false")
                    if is_given(x_llm_block_input_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Input-DOS-Detection": ("true" if x_llm_block_input_dos_detection else "false")
                    if is_given(x_llm_block_input_dos_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Input-PII": ("true" if x_llm_block_input_pii else "false")
                    if is_given(x_llm_block_input_pii)
                    else NOT_GIVEN,
                    "X-LLM-Block-Output-Code-Detection": ("true" if x_llm_block_output_code_detection else "false")
                    if is_given(x_llm_block_output_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Output-PII": ("true" if x_llm_block_output_pii else "false")
                    if is_given(x_llm_block_output_pii)
                    else NOT_GIVEN,
                    "X-LLM-Block-Prompt-Injection": ("true" if x_llm_block_prompt_injection else "false")
                    if is_given(x_llm_block_prompt_injection)
                    else NOT_GIVEN,
                    "X-LLM-Block-Unsafe": ("true" if x_llm_block_unsafe else "false")
                    if is_given(x_llm_block_unsafe)
                    else NOT_GIVEN,
                    "X-LLM-Block-Unsafe-Input": ("true" if x_llm_block_unsafe_input else "false")
                    if is_given(x_llm_block_unsafe_input)
                    else NOT_GIVEN,
                    "X-LLM-Block-Unsafe-Output": ("true" if x_llm_block_unsafe_output else "false")
                    if is_given(x_llm_block_unsafe_output)
                    else NOT_GIVEN,
                    "X-LLM-Entity-Type": str(x_llm_entity_type) if is_given(x_llm_entity_type) else NOT_GIVEN,
                    "X-LLM-Input-DOS-Detection-Threshold": x_llm_input_dos_detection_threshold,
                    "X-LLM-Prompt-Injection-Scan-Type": str(x_llm_prompt_injection_scan_type)
                    if is_given(x_llm_prompt_injection_scan_type)
                    else NOT_GIVEN,
                    "X-LLM-Redact-Input-PII": ("true" if x_llm_redact_input_pii else "false")
                    if is_given(x_llm_redact_input_pii)
                    else NOT_GIVEN,
                    "X-LLM-Redact-Output-PII": ("true" if x_llm_redact_output_pii else "false")
                    if is_given(x_llm_redact_output_pii)
                    else NOT_GIVEN,
                    "X-LLM-Redact-Type": str(x_llm_redact_type) if is_given(x_llm_redact_type) else NOT_GIVEN,
                    "X-LLM-Skip-Guardrail-Detection": ("true" if x_llm_skip_guardrail_detection else "false")
                    if is_given(x_llm_skip_guardrail_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-Code-Detection": ("true" if x_llm_skip_input_code_detection else "false")
                    if is_given(x_llm_skip_input_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-DOS-Detection": ("true" if x_llm_skip_input_dos_detection else "false")
                    if is_given(x_llm_skip_input_dos_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-PII-Detection": ("true" if x_llm_skip_input_pii_detection else "false")
                    if is_given(x_llm_skip_input_pii_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Input-URL-Detection": ("true" if x_llm_skip_input_url_detection else "false")
                    if is_given(x_llm_skip_input_url_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Output-Code-Detection": ("true" if x_llm_skip_output_code_detection else "false")
                    if is_given(x_llm_skip_output_code_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Output-PII-Detection": ("true" if x_llm_skip_output_pii_detection else "false")
                    if is_given(x_llm_skip_output_pii_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Output-URL-Detection": ("true" if x_llm_skip_output_url_detection else "false")
                    if is_given(x_llm_skip_output_url_detection)
                    else NOT_GIVEN,
                    "X-LLM-Skip-Prompt-Injection-Detection": (
                        "true" if x_llm_skip_prompt_injection_detection else "false"
                    )
                    if is_given(x_llm_skip_prompt_injection_detection)
                    else NOT_GIVEN,
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
