# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SensorQueryParams", "Filter"]


class SensorQueryParams(TypedDict, total=False):
    filter: Filter

    order_by: str

    order_dir: Literal["asc", "desc"]

    page_number: int

    page_size: int


class Filter(TypedDict, total=False):
    active: bool

    created_at_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    created_at_stop: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    plaintext_name: str

    source: Literal["adhoc"]

    version: int
