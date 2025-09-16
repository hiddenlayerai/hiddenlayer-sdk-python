# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .text_content_param import TextContentParam

__all__ = ["InputParam"]


class InputParamTyped(TypedDict, total=False):
    messages: Iterable[TextContentParam]


InputParam: TypeAlias = Union[InputParamTyped, Dict[str, object]]
