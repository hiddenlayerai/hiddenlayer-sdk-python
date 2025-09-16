# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .input_param import InputParam
from .output_param import OutputParam
from .metadata_param import MetadataParam

__all__ = ["InteractionAnalyzeParams"]


class InteractionAnalyzeParams(TypedDict, total=False):
    metadata: Required[MetadataParam]

    input: InputParam

    output: OutputParam

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]
