# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .interactions_input_param import InteractionsInputParam
from .interactions_output_param import InteractionsOutputParam
from .interactions_metadata_param import InteractionsMetadataParam

__all__ = ["InteractionAnalyzeParams"]


class InteractionAnalyzeParams(TypedDict, total=False):
    metadata: Required[InteractionsMetadataParam]

    input: InteractionsInputParam

    output: InteractionsOutputParam

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]
