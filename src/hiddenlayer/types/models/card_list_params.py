# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    limit: int

    model_name_contains: Annotated[str, PropertyInfo(alias="model_name[contains]")]
    """substring match on model name"""

    model_name_eq: Annotated[str, PropertyInfo(alias="model_name[eq]")]
    """substring match on model name"""

    offset: int

    sort: str
    """
    allow sorting by model name or created at timestamp, ascending (+) or the
    default descending (-)
    """
