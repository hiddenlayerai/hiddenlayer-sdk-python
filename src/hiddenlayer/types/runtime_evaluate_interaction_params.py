# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RuntimeEvaluateInteractionParams",
    "Interaction",
    "InteractionCanonicalInteraction",
    "InteractionCanonicalInteractionMessage",
    "InteractionCanonicalInteractionMessageContent",
    "InteractionCanonicalInteractionMessageContentTextPart",
    "InteractionCanonicalInteractionMessageContentToolUsePart",
    "InteractionCanonicalInteractionMessageContentToolResultPart",
    "InteractionCanonicalInteractionMessageTimestamp",
    "InteractionCanonicalInteractionToolsAvailable",
    "Metadata",
]


class RuntimeEvaluateInteractionParams(TypedDict, total=False):
    interaction: Required[Interaction]
    """The interaction to evaluate.

    Accepts either the canonical form (`CanonicalInteraction` — `messages` and
    optional `tools_available`) or a native LLM-provider payload passed through
    verbatim. Supported provider formats are OpenAI Chat Completions, OpenAI
    Responses, and Anthropic Messages. `ProviderPayload` is intentionally permissive
    (any JSON object) so callers can supply provider-native shapes without schema
    constraints.
    """

    metadata: Required[Metadata]
    """Metadata about the LLM interactions being evaluated."""

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]


class InteractionCanonicalInteractionMessageContentTextPart(TypedDict, total=False):
    """A text content part within a message."""

    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """Content part type for text."""


class InteractionCanonicalInteractionMessageContentToolUsePart(TypedDict, total=False):
    """A tool invocation part representing a tool call by the assistant."""

    id: Required[str]
    """Tool call identifier. Used to correlate tool invocations with their results."""

    tool_name: Required[str]
    """Name of the tool being invoked."""

    type: Required[Literal["tool_use"]]
    """Content part type for tool invocation."""

    tool_input: Dict[str, object]
    """Tool arguments/input as a key-value object."""


class InteractionCanonicalInteractionMessageContentToolResultPart(TypedDict, total=False):
    """A tool result part containing the output from a tool execution."""

    id: Required[str]
    """Tool call identifier.

    Used to correlate this result with the original tool invocation.
    """

    result: Required[str]
    """The tool execution result content."""

    type: Required[Literal["tool_result"]]
    """Content part type for tool result."""

    success: bool
    """Whether the tool execution succeeded."""


InteractionCanonicalInteractionMessageContent: TypeAlias = Union[
    InteractionCanonicalInteractionMessageContentTextPart,
    InteractionCanonicalInteractionMessageContentToolUsePart,
    InteractionCanonicalInteractionMessageContentToolResultPart,
]


class InteractionCanonicalInteractionMessageTimestamp(TypedDict, total=False):
    """Optional timestamp for when this message was created.

    When supplied, `value` is required.
    """

    value: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp in ISO 8601 / RFC 3339 format."""


class InteractionCanonicalInteractionMessage(TypedDict, total=False):
    """
    Base schema for a conversation message in normalized/canonical form.
    Represents the unified representation of messages across different LLM providers.
    """

    content: Required[Iterable[InteractionCanonicalInteractionMessageContent]]
    """
    Array of content parts representing the message content. Each part has a `type`
    field indicating the content type.
    """

    role: Required[str]
    """The role of the message sender. Standard roles include:

    - `user`: End-user input
    - `assistant`: LLM/agent response
    - `system`: System instructions or context
    - `tool`: Tool result message
    """

    timestamp: InteractionCanonicalInteractionMessageTimestamp
    """Optional timestamp for when this message was created.

    When supplied, `value` is required.
    """


class InteractionCanonicalInteractionToolsAvailable(TypedDict, total=False):
    """
    Base schema for a tool definition available to the model.
    Represents the canonical form of tool definitions across different LLM providers.
    """

    name: Required[str]
    """Name of the tool."""

    description: str
    """Human-readable description of what the tool does."""

    parameters: Dict[str, object]
    """
    JSON Schema defining the tool's input parameters. Stored as a flexible object to
    support various schema formats.
    """


class InteractionCanonicalInteraction(TypedDict, total=False):
    """
    The canonical (provider-agnostic) form of an LLM interaction: an ordered
    sequence of messages, optionally with the tool catalog that was in scope.
    Use this form to evaluate interactions independently of any specific
    provider's payload structure.
    """

    messages: Required[Iterable[InteractionCanonicalInteractionMessage]]
    """Ordered sequence of messages to evaluate, in chronological order.

    May contain any combination of user input, assistant output, system prompts, and
    tool calls/results — and may be a single message or many. There is no
    requirement that the messages form a complete request/response pair.
    """

    tools_available: Iterable[InteractionCanonicalInteractionToolsAvailable]
    """Tool definitions available to the model in the context of these messages."""


Interaction: TypeAlias = Union[InteractionCanonicalInteraction, Dict[str, object]]


class Metadata(TypedDict, total=False):
    """Metadata about the LLM interactions being evaluated."""

    model: Required[str]
    """The model identifier used for the interaction."""

    provider: Required[str]
    """The LLM provider (e.g., openai, anthropic, azure, bedrock)."""

    requester_id: Required[str]
    """
    Identifier for the entity making the request. Could be a user ID, service
    account, or agent identifier.
    """

    external_session_id: str
    """
    An externally-defined session identifier to group interactions into a single
    session. The identifier should be unique across all sessions.
    """
