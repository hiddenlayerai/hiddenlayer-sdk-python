# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["InteractionAnalyzeParams", "Metadata", "Input", "InputMessage", "Output", "OutputMessage"]


class InteractionAnalyzeParams(TypedDict, total=False):
    metadata: Required[Metadata]

    input: Input

    output: Output

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]


class Metadata(TypedDict, total=False):
    model: Required[str]
    """The language model for the interactions."""

    requester_id: Required[str]
    """The identifier for the entity making the interactions."""

    provider: str
    """The provider of the language model."""


class InputMessage(TypedDict, total=False):
    content: Required[str]
    """The textual content of the message."""

    role: str
    """The role of the message sender (e.g., user, assistant, system)."""


class InputTyped(TypedDict, total=False):
    messages: Iterable[InputMessage]
    """The list of messages as input to a language model."""


Input: TypeAlias = Union[InputTyped, Dict[str, object]]


class OutputMessage(TypedDict, total=False):
    content: Required[str]
    """The textual content of the message."""

    role: str
    """The role of the message sender (e.g., user, assistant, system)."""


class Output(TypedDict, total=False):
    messages: Iterable[OutputMessage]
    """The list of messages as output from a language model."""
