# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PromptAnalyzerCreateResponse",
    "Categories",
    "Frameworks",
    "FrameworksMitre",
    "FrameworksOwasp",
    "FrameworksOwasp2025",
    "Policy",
    "Response",
    "Results",
    "ResultsGuardrailResults",
    "ResultsGuardrailResultsRefusalClassifierResults",
    "ResultsInputBlockListResults",
    "ResultsInputCodeResults",
    "ResultsInputDosResults",
    "ResultsInputLanguageResults",
    "ResultsInputPiiResults",
    "ResultsInputURLResults",
    "ResultsOutputCodeResults",
    "ResultsOutputPiiResults",
    "ResultsOutputURLResults",
    "ResultsPromptInjectionClassifierResult",
]


class Categories(BaseModel):
    """The analysis detection categories"""

    guardrail: Optional[bool] = None
    """The input activated the upstream guardrails"""

    input_code: Optional[bool] = None
    """The input contains code"""

    input_dos: Optional[bool] = None
    """The input contains a denial of service attack"""

    input_language: Optional[bool] = None
    """The input contains a disallowed language"""

    input_pii: Optional[bool] = None
    """The input contains personally identifiable information"""

    output_code: Optional[bool] = None
    """The output contains code"""

    output_pii: Optional[bool] = None
    """The output contains personally identifiable information"""

    prompt_injection: Optional[bool] = None
    """The input contains prompt injection"""

    unsafe_input: Optional[bool] = None
    """The input is unsafe"""

    unsafe_output: Optional[bool] = None
    """The output is unsafe"""


class FrameworksMitre(BaseModel):
    """The MITRE Atlas framework labels identified during analysis"""

    label: Optional[str] = None
    """The label of the MITRE Atlas framework label"""

    name: Optional[str] = None
    """The name of the MITRE Atlas framework label"""


class FrameworksOwasp(BaseModel):
    """The OWASP framework labels identified during analysis"""

    label: Optional[str] = None
    """The label of the OWASP framework label"""

    name: Optional[str] = None
    """The name of the OWASP framework label"""


class FrameworksOwasp2025(BaseModel):
    """The OWASP:2025 framework labels identified during analysis"""

    label: Optional[str] = None
    """The label of the OWASP:2025 framework label"""

    name: Optional[str] = None
    """The name of the OWASP:2025 framework label"""


class Frameworks(BaseModel):
    """The framework labels identified during analysis"""

    mitre: Optional[List[FrameworksMitre]] = None

    owasp: Optional[List[FrameworksOwasp]] = None

    owasp_2025: Optional[List[FrameworksOwasp2025]] = FieldInfo(alias="owasp:2025", default=None)


class Policy(BaseModel):
    """The policy used during analysis"""

    block_guardrail_detection: Optional[bool] = None
    """Block guardrail detection"""

    block_input_code_detection: Optional[bool] = None
    """Block input code detection"""

    block_input_dos_detection: Optional[bool] = None
    """Block input denial of service detection"""

    block_input_pii: Optional[bool] = None
    """Block input personally identifiable information"""

    block_output_code_detection: Optional[bool] = None
    """Block output code detection"""

    block_output_pii: Optional[bool] = None
    """Block output personally identifiable information"""

    block_prompt_injection: Optional[bool] = None
    """Block prompt injection"""

    block_unsafe: Optional[bool] = None
    """Block unsafe input and output"""

    block_unsafe_input: Optional[bool] = None
    """Block unsafe input"""

    block_unsafe_output: Optional[bool] = None
    """Block unsafe output"""

    entity_type: Optional[Literal["strict", "all"]] = None
    """The type of entity to redact"""

    input_dos_detection_threshold: Optional[float] = None
    """The threshold for input denial of service detection"""

    prompt_injection_scan_type: Optional[Literal["quick", "full"]] = None
    """The type of prompt injection scan to use"""

    redact_input_pii: Optional[bool] = None
    """Redact input personally identifiable information"""

    redact_output_pii: Optional[bool] = None
    """Redact output personally identifiable information"""

    redact_type: Optional[Literal["entity", "strict"]] = None
    """The type of redaction to use"""

    skip_guardrail_detection: Optional[bool] = None
    """Skip guardrail detection"""

    skip_input_code_detection: Optional[bool] = None
    """Skip input code detection"""

    skip_input_dos_detection: Optional[bool] = None
    """Skip input denial of service detection"""

    skip_input_pii_detection: Optional[bool] = None
    """Skip input personally identifiable information detection"""

    skip_input_url_detection: Optional[bool] = None
    """Skip input URL detection"""

    skip_output_code_detection: Optional[bool] = None
    """Skip output code detection"""

    skip_output_pii_detection: Optional[bool] = None
    """Skip output personally identifiable information detection"""

    skip_output_url_detection: Optional[bool] = None
    """Skip output URL detection"""

    skip_prompt_injection_detection: Optional[bool] = None
    """Skip prompt injection detection"""


class Response(BaseModel):
    model: Optional[str] = None

    output: Optional[str] = None

    prompt: Optional[str] = None

    provider: Optional[str] = None

    unmodified_output: Optional[str] = None

    unmodified_prompt: Optional[str] = None


class ResultsGuardrailResultsRefusalClassifierResults(BaseModel):
    """The refusal classifier results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the refusal classifier"""

    probabilities: Optional[List[float]] = None

    verdict: Optional[bool] = None
    """The verdict of the refusal classifier"""

    version: Optional[float] = None
    """The version of the refusal classifier"""


class ResultsGuardrailResults(BaseModel):
    """The guardrail results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the guardrail"""

    refusal_classifier_results: Optional[ResultsGuardrailResultsRefusalClassifierResults] = None
    """The refusal classifier results"""

    verdict: Optional[bool] = None
    """The verdict of the guardrail analysis"""


class ResultsInputBlockListResults(BaseModel):
    """The input block list results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the input block list"""

    matches: Optional[List[str]] = None

    verdict: Optional[bool] = None
    """The verdict of the input block list analysis"""


class ResultsInputCodeResults(BaseModel):
    """The input code results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the input code"""

    verdict: Optional[bool] = None
    """The verdict of the input code analysis"""


class ResultsInputDosResults(BaseModel):
    """The input denial of service results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the input denial of service"""

    embeddings_length: Optional[float] = None
    """The length of the embeddings analyzed"""

    verdict: Optional[bool] = None
    """The verdict of the input denial of service analysis"""


class ResultsInputLanguageResults(BaseModel):
    """The input language results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the input language detection"""

    language: Optional[str] = None
    """Language detected in the input"""

    verdict: Optional[bool] = None
    """The verdict of the input language analysis"""


class ResultsInputPiiResults(BaseModel):
    """The input personally identifiable information results"""

    elapsed_ms: Optional[float] = None
    """
    The time in milliseconds it took to process the input personally identifiable
    information
    """

    entities: Optional[List[str]] = None

    verdict: Optional[bool] = None
    """The verdict of the input personally identifiable information analysis"""


class ResultsInputURLResults(BaseModel):
    """The input URL results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the guardrail"""

    urls: Optional[List[str]] = None


class ResultsOutputCodeResults(BaseModel):
    """The output code results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the output code"""

    verdict: Optional[bool] = None
    """The verdict of the output code analysis"""


class ResultsOutputPiiResults(BaseModel):
    """The output personally identifiable information results"""

    elapsed_ms: Optional[float] = None
    """
    The time in milliseconds it took to process the output personally identifiable
    information
    """

    entities: Optional[List[str]] = None

    verdict: Optional[bool] = None
    """The verdict of the output personally identifiable information analysis"""


class ResultsOutputURLResults(BaseModel):
    """The output URL results"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the guardrail"""

    urls: Optional[List[str]] = None


class ResultsPromptInjectionClassifierResult(BaseModel):
    allow_override: Optional[str] = None
    """The allow override applied to the prompt"""

    block_override: Optional[str] = None
    """The block override applied to the prompt"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the prompt injection classifier"""

    probabilities: Optional[List[float]] = None

    verdict: Optional[bool] = None
    """The verdict of the prompt injection classifier"""

    version: Optional[float] = None
    """The version of the prompt injection classifier"""


class Results(BaseModel):
    """The analysis results"""

    guardrail_results: Optional[ResultsGuardrailResults] = None
    """The guardrail results"""

    input_block_list_results: Optional[ResultsInputBlockListResults] = None
    """The input block list results"""

    input_code_results: Optional[ResultsInputCodeResults] = None
    """The input code results"""

    input_dos_results: Optional[ResultsInputDosResults] = None
    """The input denial of service results"""

    input_language_results: Optional[ResultsInputLanguageResults] = None
    """The input language results"""

    input_pii_results: Optional[ResultsInputPiiResults] = None
    """The input personally identifiable information results"""

    input_url_results: Optional[ResultsInputURLResults] = None
    """The input URL results"""

    output_code_results: Optional[ResultsOutputCodeResults] = None
    """The output code results"""

    output_pii_results: Optional[ResultsOutputPiiResults] = None
    """The output personally identifiable information results"""

    output_url_results: Optional[ResultsOutputURLResults] = None
    """The output URL results"""

    prompt_injection_classifier_results: Optional[List[ResultsPromptInjectionClassifierResult]] = None


class PromptAnalyzerCreateResponse(BaseModel):
    categories: Optional[Categories] = None
    """The analysis detection categories"""

    elapsed_ms: Optional[float] = None
    """The time in milliseconds it took to process the request"""

    frameworks: Optional[Frameworks] = None
    """The framework labels identified during analysis"""

    model: Optional[str] = None

    policy: Optional[Policy] = None
    """The policy used during analysis"""

    provider: Optional[str] = None

    response: Optional[Response] = None

    results: Optional[Results] = None
    """The analysis results"""

    upstream_elapsed_ms: Optional[float] = None
    """The time in milliseconds the upstream LLM took to process the request"""

    verdict: Optional[bool] = None
    """The overall verdict of the analysis"""
