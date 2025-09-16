# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["InteractionsMetadataParam"]


class InteractionsMetadataParamTyped(TypedDict, total=False):
    model: Required[str]

    requester_id: Required[str]

    provider: str


InteractionsMetadataParam: TypeAlias = Union[InteractionsMetadataParamTyped, Dict[str, object]]
