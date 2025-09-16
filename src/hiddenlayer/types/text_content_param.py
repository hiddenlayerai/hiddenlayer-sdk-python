# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["TextContentParam"]


class TextContentParamTyped(TypedDict, total=False):
    content: Required[str]

    role: str


TextContentParam: TypeAlias = Union[TextContentParamTyped, Dict[str, object]]
