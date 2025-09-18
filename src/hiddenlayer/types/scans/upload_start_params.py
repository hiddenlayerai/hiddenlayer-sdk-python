# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UploadStartParams"]


class UploadStartParams(TypedDict, total=False):
    model_name: Required[str]
    """Model name"""

    model_version: Required[str]
    """Model version"""

    requesting_entity: Required[str]
    """Requesting entity"""

    location_alias: str
    """Requested location alias"""

    origin: str
    """
    Specifies the platform or service where the model originated before being
    scanned
    """

    request_source: Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload"]
    """Identifies the system that requested the scan"""

    x_correlation_id: Annotated[str, PropertyInfo(alias="X-Correlation-Id")]
