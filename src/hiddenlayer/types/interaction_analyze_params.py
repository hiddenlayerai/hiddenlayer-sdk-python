# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .interactions_input_param import InteractionsInputParam
from .interactions_output_param import InteractionsOutputParam

__all__ = ["InteractionAnalyzeParams", "Metadata"]


class InteractionAnalyzeParams(TypedDict, total=False):
    metadata: Required[Metadata]

    input: InteractionsInputParam

    output: InteractionsOutputParam

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]


class MetadataTyped(TypedDict, total=False):
    model: Required[str]

    requester_id: Required[str]

    provider: str


Metadata: TypeAlias = Union[MetadataTyped, Dict[str, object]]
