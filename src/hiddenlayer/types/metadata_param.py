# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["MetadataParam"]


class MetadataParamTyped(TypedDict, total=False):
    model: Required[str]

    requester_id: Required[str]

    provider: str


MetadataParam: TypeAlias = Union[MetadataParamTyped, Dict[str, object]]
