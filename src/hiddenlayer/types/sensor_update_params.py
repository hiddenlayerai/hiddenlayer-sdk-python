# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SensorUpdateParams"]


class SensorUpdateParams(TypedDict, total=False):
    active: bool

    plaintext_name: str

    tags: Dict[str, object]

    x_correlation_id: Annotated[str, PropertyInfo(alias="X-Correlation-Id")]
