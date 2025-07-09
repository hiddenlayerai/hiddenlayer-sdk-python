# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobRetrieveParams"]


class JobRetrieveParams(TypedDict, total=False):
    x_correlation_id: Required[Annotated[str, PropertyInfo(alias="X-Correlation-Id")]]

    has_detections: bool
    """Filter file_results to only those that have detections (and parents)"""
