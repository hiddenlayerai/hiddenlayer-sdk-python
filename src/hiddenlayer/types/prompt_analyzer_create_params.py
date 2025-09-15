# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromptAnalyzerCreateParams"]


class PromptAnalyzerCreateParams(TypedDict, total=False):
    prompt: Required[str]

    model: str

    output: str

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]

    x_llm_block_guardrail_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Guardrail-Detection")]

    x_llm_block_input_code_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Input-Code-Detection")]

    x_llm_block_input_dos_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Input-DOS-Detection")]

    x_llm_block_input_pii: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Input-PII")]

    x_llm_block_output_code_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Output-Code-Detection")]

    x_llm_block_output_pii: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Output-PII")]

    x_llm_block_prompt_injection: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Prompt-Injection")]

    x_llm_block_unsafe: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Unsafe")]

    x_llm_block_unsafe_input: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Unsafe-Input")]

    x_llm_block_unsafe_output: Annotated[bool, PropertyInfo(alias="X-LLM-Block-Unsafe-Output")]

    x_llm_entity_type: Annotated[Literal["strict", "all"], PropertyInfo(alias="X-LLM-Entity-Type")]
    """The type of entity to redact"""

    x_llm_input_dos_detection_threshold: Annotated[str, PropertyInfo(alias="X-LLM-Input-DOS-Detection-Threshold")]

    x_llm_prompt_injection_scan_type: Annotated[
        Literal["quick", "full"], PropertyInfo(alias="X-LLM-Prompt-Injection-Scan-Type")
    ]
    """The type of prompt injection scan to use"""

    x_llm_redact_input_pii: Annotated[bool, PropertyInfo(alias="X-LLM-Redact-Input-PII")]

    x_llm_redact_output_pii: Annotated[bool, PropertyInfo(alias="X-LLM-Redact-Output-PII")]

    x_llm_redact_type: Annotated[Literal["entity", "strict"], PropertyInfo(alias="X-LLM-Redact-Type")]
    """The type of redaction to use"""

    x_llm_skip_guardrail_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Guardrail-Detection")]

    x_llm_skip_input_code_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Input-Code-Detection")]

    x_llm_skip_input_dos_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Input-DOS-Detection")]

    x_llm_skip_input_pii_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Input-PII-Detection")]

    x_llm_skip_input_url_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Input-URL-Detection")]

    x_llm_skip_output_code_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Output-Code-Detection")]

    x_llm_skip_output_pii_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Output-PII-Detection")]

    x_llm_skip_output_url_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Output-URL-Detection")]

    x_llm_skip_prompt_injection_detection: Annotated[bool, PropertyInfo(alias="X-LLM-Skip-Prompt-Injection-Detection")]

    x_requester_id: Annotated[str, PropertyInfo(alias="X-Requester-Id")]
