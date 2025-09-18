# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SensorCreateParams"]


class SensorCreateParams(TypedDict, total=False):
    plaintext_name: Required[str]

    active: bool

    adhoc: bool

    tags: Dict[str, object]

    version: int

    x_correlation_id: Annotated[str, PropertyInfo(alias="X-Correlation-Id")]
