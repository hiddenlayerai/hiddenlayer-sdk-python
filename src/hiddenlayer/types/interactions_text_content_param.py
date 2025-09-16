# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["InteractionsTextContentParam"]


class InteractionsTextContentParamTyped(TypedDict, total=False):
    content: Required[str]

    role: str


InteractionsTextContentParam: TypeAlias = Union[InteractionsTextContentParamTyped, Dict[str, object]]
