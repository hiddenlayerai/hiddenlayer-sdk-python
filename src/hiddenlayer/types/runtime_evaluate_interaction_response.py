# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "RuntimeEvaluateInteractionResponse",
    "EvaluatedInteraction",
    "EvaluatedInteractionMessage",
    "EvaluatedInteractionMessageContent",
    "EvaluatedInteractionMessageContentTextPart",
    "EvaluatedInteractionMessageContentToolUsePart",
    "EvaluatedInteractionMessageContentToolResultPart",
    "EvaluatedInteractionMessageAnalysis",
    "EvaluatedInteractionMessageTimestamp",
    "EvaluatedInteractionToolsAvailable",
    "Metadata",
    "MetadataProject",
    "Outcome",
    "OutcomeDetection",
    "OutcomeEffectiveInteraction",
    "OutcomeEffectiveInteractionCanonicalInteraction",
    "OutcomeEffectiveInteractionCanonicalInteractionMessage",
    "OutcomeEffectiveInteractionCanonicalInteractionMessageContent",
    "OutcomeEffectiveInteractionCanonicalInteractionMessageContentTextPart",
    "OutcomeEffectiveInteractionCanonicalInteractionMessageContentToolUsePart",
    "OutcomeEffectiveInteractionCanonicalInteractionMessageContentToolResultPart",
    "OutcomeEffectiveInteractionCanonicalInteractionMessageTimestamp",
    "OutcomeEffectiveInteractionCanonicalInteractionToolsAvailable",
]


class EvaluatedInteractionMessageContentTextPart(BaseModel):
    """A text content part within a message."""

    text: str
    """The text content."""

    type: Literal["text"]
    """Content part type for text."""


class EvaluatedInteractionMessageContentToolUsePart(BaseModel):
    """A tool invocation part representing a tool call by the assistant."""

    id: str
    """Tool call identifier. Used to correlate tool invocations with their results."""

    tool_name: str
    """Name of the tool being invoked."""

    type: Literal["tool_use"]
    """Content part type for tool invocation."""

    tool_input: Optional[Dict[str, object]] = None
    """Tool arguments/input as a key-value object."""


class EvaluatedInteractionMessageContentToolResultPart(BaseModel):
    """A tool result part containing the output from a tool execution."""

    id: str
    """Tool call identifier.

    Used to correlate this result with the original tool invocation.
    """

    result: str
    """The tool execution result content."""

    type: Literal["tool_result"]
    """Content part type for tool result."""

    success: Optional[bool] = None
    """Whether the tool execution succeeded."""


EvaluatedInteractionMessageContent: TypeAlias = Annotated[
    Union[
        EvaluatedInteractionMessageContentTextPart,
        EvaluatedInteractionMessageContentToolUsePart,
        EvaluatedInteractionMessageContentToolResultPart,
    ],
    PropertyInfo(discriminator="type"),
]


class EvaluatedInteractionMessageAnalysis(BaseModel):
    """Per-message security analysis from signal extraction.

    `signals` mirrors
    the production-signals dictionary fed into the policy evaluation
    context — each key is a signal name (e.g., `prompt_injection`, `code`),
    each value is the opaque finding object that signal produced.
    """

    signals: Dict[str, Dict[str, object]]
    """
    Production signal findings for this message, keyed by signal name. All known
    production signal types are always present (populated with schema defaults when
    nothing fired). Values are opaque finding objects whose internal shape may
    evolve.
    """


class EvaluatedInteractionMessageTimestamp(BaseModel):
    """Optional timestamp for when this message was created.

    When supplied, `value` is required.
    """

    value: datetime
    """The timestamp in ISO 8601 / RFC 3339 format."""


class EvaluatedInteractionMessage(BaseModel):
    """
    Base schema for a conversation message in normalized/canonical form.
    Represents the unified representation of messages across different LLM providers.
    """

    content: List[EvaluatedInteractionMessageContent]
    """
    Array of content parts representing the message content. Each part has a `type`
    field indicating the content type.
    """

    role: str
    """The role of the message sender. Standard roles include:

    - `user`: End-user input
    - `assistant`: LLM/agent response
    - `system`: System instructions or context
    - `tool`: Tool result message
    """

    analysis: Optional[EvaluatedInteractionMessageAnalysis] = None
    """Per-message security analysis from signal extraction.

    `signals` mirrors the production-signals dictionary fed into the policy
    evaluation context — each key is a signal name (e.g., `prompt_injection`,
    `code`), each value is the opaque finding object that signal produced.
    """

    timestamp: Optional[EvaluatedInteractionMessageTimestamp] = None
    """Optional timestamp for when this message was created.

    When supplied, `value` is required.
    """


class EvaluatedInteractionToolsAvailable(BaseModel):
    """
    Base schema for a tool definition available to the model.
    Represents the canonical form of tool definitions across different LLM providers.
    """

    name: str
    """Name of the tool."""

    description: Optional[str] = None
    """Human-readable description of what the tool does."""

    parameters: Optional[Dict[str, object]] = None
    """
    JSON Schema defining the tool's input parameters. Stored as a flexible object to
    support various schema formats.
    """


class EvaluatedInteraction(BaseModel):
    """
    The canonicalized interaction as seen by the evaluator — messages and
    tool catalog — annotated per-message with signals and their findings.
    Used for `evaluated_interaction` regardless of which form the request
    supplied: when the request used a native provider payload, the
    evaluator canonicalizes it into this shape so detection rules can
    target a uniform structure.
    """

    messages: List[EvaluatedInteractionMessage]
    """Ordered sequence of canonicalized messages.

    Each message is annotated with the signals that fired against it (and findings
    produced by those signals).
    """

    tools_available: Optional[List[EvaluatedInteractionToolsAvailable]] = None
    """
    The canonicalized tool catalog that was in scope during evaluation. Present only
    when tools were provided in the request.
    """


class MetadataProject(BaseModel):
    """Project context resolved for this evaluation."""

    configuration_id: str
    """The unique identifier for the Configuration used during evaluation."""

    policy_id: str
    """The unique identifier for the Policy applied to this interaction."""

    project_id: str
    """The unique identifier for the Project."""

    project_alias: Optional[str] = None
    """A custom alias for the Project."""


class Metadata(BaseModel):
    """Metadata about the completed evaluation of the interactions."""

    evaluated_at: datetime
    """Timestamp when the evaluation was performed."""

    evaluation_id: str
    """Server-generated unique identifier for this evaluation.

    Persisted on the stored interaction record and referenced in structured logs for
    correlation.
    """

    model: str
    """The model identifier from the request."""

    processing_time_ms: float
    """Total time taken to perform the evaluation, in milliseconds."""

    project: MetadataProject
    """Project context resolved for this evaluation."""

    provider: str
    """The LLM provider from the request."""

    requester_id: str
    """The requester identifier from the request."""


class OutcomeDetection(BaseModel):
    """
    A security detection from policy evaluation with risk assessment.
    Detections are composite results produced by detection rules running against
    the evaluation context (`evaluated_interaction`). Supporting evidence is not
    duplicated on the detection itself — it is observable in `evaluated_interaction`
    via the signals and findings that the rule matched.
    """

    risk_level: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    """Categorical risk level for this detection."""

    rule_name: str
    """
    The human-readable name of the detection rule (e.g., prompt_injection,
    sensitive_pii_exposed).
    """


class OutcomeEffectiveInteractionCanonicalInteractionMessageContentTextPart(BaseModel):
    """A text content part within a message."""

    text: str
    """The text content."""

    type: Literal["text"]
    """Content part type for text."""


class OutcomeEffectiveInteractionCanonicalInteractionMessageContentToolUsePart(BaseModel):
    """A tool invocation part representing a tool call by the assistant."""

    id: str
    """Tool call identifier. Used to correlate tool invocations with their results."""

    tool_name: str
    """Name of the tool being invoked."""

    type: Literal["tool_use"]
    """Content part type for tool invocation."""

    tool_input: Optional[Dict[str, object]] = None
    """Tool arguments/input as a key-value object."""


class OutcomeEffectiveInteractionCanonicalInteractionMessageContentToolResultPart(BaseModel):
    """A tool result part containing the output from a tool execution."""

    id: str
    """Tool call identifier.

    Used to correlate this result with the original tool invocation.
    """

    result: str
    """The tool execution result content."""

    type: Literal["tool_result"]
    """Content part type for tool result."""

    success: Optional[bool] = None
    """Whether the tool execution succeeded."""


OutcomeEffectiveInteractionCanonicalInteractionMessageContent: TypeAlias = Annotated[
    Union[
        OutcomeEffectiveInteractionCanonicalInteractionMessageContentTextPart,
        OutcomeEffectiveInteractionCanonicalInteractionMessageContentToolUsePart,
        OutcomeEffectiveInteractionCanonicalInteractionMessageContentToolResultPart,
    ],
    PropertyInfo(discriminator="type"),
]


class OutcomeEffectiveInteractionCanonicalInteractionMessageTimestamp(BaseModel):
    """Optional timestamp for when this message was created.

    When supplied, `value` is required.
    """

    value: datetime
    """The timestamp in ISO 8601 / RFC 3339 format."""


class OutcomeEffectiveInteractionCanonicalInteractionMessage(BaseModel):
    """
    Base schema for a conversation message in normalized/canonical form.
    Represents the unified representation of messages across different LLM providers.
    """

    content: List[OutcomeEffectiveInteractionCanonicalInteractionMessageContent]
    """
    Array of content parts representing the message content. Each part has a `type`
    field indicating the content type.
    """

    role: str
    """The role of the message sender. Standard roles include:

    - `user`: End-user input
    - `assistant`: LLM/agent response
    - `system`: System instructions or context
    - `tool`: Tool result message
    """

    timestamp: Optional[OutcomeEffectiveInteractionCanonicalInteractionMessageTimestamp] = None
    """Optional timestamp for when this message was created.

    When supplied, `value` is required.
    """


class OutcomeEffectiveInteractionCanonicalInteractionToolsAvailable(BaseModel):
    """
    Base schema for a tool definition available to the model.
    Represents the canonical form of tool definitions across different LLM providers.
    """

    name: str
    """Name of the tool."""

    description: Optional[str] = None
    """Human-readable description of what the tool does."""

    parameters: Optional[Dict[str, object]] = None
    """
    JSON Schema defining the tool's input parameters. Stored as a flexible object to
    support various schema formats.
    """


class OutcomeEffectiveInteractionCanonicalInteraction(BaseModel):
    """
    The canonical (provider-agnostic) form of an LLM interaction: an ordered
    sequence of messages, optionally with the tool catalog that was in scope.
    Use this form to evaluate interactions independently of any specific
    provider's payload structure.
    """

    messages: List[OutcomeEffectiveInteractionCanonicalInteractionMessage]
    """Ordered sequence of messages to evaluate, in chronological order.

    May contain any combination of user input, assistant output, system prompts, and
    tool calls/results — and may be a single message or many. There is no
    requirement that the messages form a complete request/response pair.
    """

    tools_available: Optional[List[OutcomeEffectiveInteractionCanonicalInteractionToolsAvailable]] = None
    """Tool definitions available to the model in the context of these messages."""


OutcomeEffectiveInteraction: TypeAlias = Union[OutcomeEffectiveInteractionCanonicalInteraction, Dict[str, object]]


class Outcome(BaseModel):
    """The policy outcome for the evaluated interactions.

    Carries the enforcement
    action, threat level, any detections produced by detection rules against
    `evaluated_interaction`, and the effective payload the caller should forward.
    """

    action: Literal["NONE", "DETECT", "REDACT", "BLOCK"]
    """The action applied based on policy evaluation.

    `NONE` means policy evaluation produced no detections — either no rules fired or
    no findings were emitted; the `detections` array is empty and the effective
    payload is unchanged.

    `DETECT`, `REDACT`, and `BLOCK` all mean one or more detections were produced;
    they differ in what the policy did with the payload. `DETECT` is an intentional
    observe-only outcome (detections are surfaced but the effective payload is
    unchanged); `REDACT` modifies the payload in place; `BLOCK` substitutes a canned
    block response.
    """

    detections: List[OutcomeDetection]
    """
    Security detections produced by detection rules running against the evaluation
    context. Always present; an empty array means no rules triggered.
    """

    effective_interaction: OutcomeEffectiveInteraction
    """The payload the caller should forward downstream.

    Mirrors the shape of the request's `interaction` field: if the request supplied
    the canonical form (`CanonicalInteraction`), the response returns the canonical
    form here; if the request supplied a native LLM-provider payload (OpenAI Chat
    Completions, OpenAI Responses, or Anthropic Messages), the response returns that
    same provider-native shape. Any redactions, substitutions, or tool modifications
    from the outcome's `action` are applied in place.
    """

    threat_level: Literal["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
    """
    The highest threat level across all detections, based on interaction analysis
    and configured tenant security rules. Values are ordered by severity from least
    to most: NONE, LOW, MEDIUM, HIGH, CRITICAL.
    """


class RuntimeEvaluateInteractionResponse(BaseModel):
    """
    Response payload from synchronous evaluation of an LLM interaction.
    Contains metadata about the call, the evaluation context
    (`evaluated_interaction`) that detection rules ran against, and the
    policy outcome — which carries the enforcement action, threat level,
    detections, and the effective payload the caller should forward
    (`outcome.effective_interaction`).

    `evaluated_interaction` is always the canonicalized form of the request,
    enriched per-message with signals and findings from signal extraction —
    a uniform shape that detection rules target regardless of which form
    the request supplied. `outcome.effective_interaction` mirrors the shape
    of the request's `interaction` field — canonical or provider-native —
    with any redactions, substitutions, or tool modifications from the
    outcome's action applied in place.
    """

    evaluated_interaction: EvaluatedInteraction
    """
    The canonicalized interaction as seen by the evaluator — messages and tool
    catalog — annotated per-message with signals and their findings. Used for
    `evaluated_interaction` regardless of which form the request supplied: when the
    request used a native provider payload, the evaluator canonicalizes it into this
    shape so detection rules can target a uniform structure.
    """

    metadata: Metadata
    """Metadata about the completed evaluation of the interactions."""

    outcome: Outcome
    """The policy outcome for the evaluated interactions.

    Carries the enforcement action, threat level, any detections produced by
    detection rules against `evaluated_interaction`, and the effective payload the
    caller should forward.
    """
