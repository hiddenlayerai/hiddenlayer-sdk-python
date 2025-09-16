# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .interactions_text_content_param import InteractionsTextContentParam

__all__ = ["InteractionsInputParam"]


class InteractionsInputParamTyped(TypedDict, total=False):
    messages: Iterable[InteractionsTextContentParam]


InteractionsInputParam: TypeAlias = Union[InteractionsInputParamTyped, Dict[str, object]]
