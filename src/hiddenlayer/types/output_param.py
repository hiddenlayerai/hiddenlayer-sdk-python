# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .text_content_param import TextContentParam

__all__ = ["OutputParam"]


class OutputParamTyped(TypedDict, total=False):
    messages: Iterable[TextContentParam]


OutputParam: TypeAlias = Union[OutputParamTyped, Dict[str, object]]
