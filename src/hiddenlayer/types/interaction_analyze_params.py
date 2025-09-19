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

    x_correlation_id: Annotated[str, PropertyInfo(alias="X-Correlation-Id")]


class MetadataTyped(TypedDict, total=False):
    model: Required[str]

    requester_id: Required[str]

    provider: str


Metadata: TypeAlias = Union[MetadataTyped, Dict[str, object]]


class InputMessageTyped(TypedDict, total=False):
    content: Required[str]

    role: str


InputMessage: TypeAlias = Union[InputMessageTyped, Dict[str, object]]


class InputTyped(TypedDict, total=False):
    messages: Iterable[InputMessage]


Input: TypeAlias = Union[InputTyped, Dict[str, object]]


class OutputMessageTyped(TypedDict, total=False):
    content: Required[str]

    role: str


OutputMessage: TypeAlias = Union[OutputMessageTyped, Dict[str, object]]


class OutputTyped(TypedDict, total=False):
    messages: Iterable[OutputMessage]


Output: TypeAlias = Union[OutputTyped, Dict[str, object]]
