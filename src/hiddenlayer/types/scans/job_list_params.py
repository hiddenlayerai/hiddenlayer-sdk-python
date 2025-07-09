# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobListParams", "ModelName", "Source"]


class JobListParams(TypedDict, total=False):
    x_correlation_id: Required[Annotated[str, PropertyInfo(alias="X-Correlation-Id")]]

    detection_category: str
    """filter by a single detection category"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End Time"""

    latest_per_model_version_only: bool
    """only return latest result per model version"""

    limit: int

    model_ids: List[str]
    """Model ID"""

    model_name: ModelName
    """filter by the model name"""

    model_version_ids: List[str]
    """Model Version IDs"""

    offset: int

    scanner_version: str
    """filter by version of the scanner"""

    severity: List[str]
    """Severities"""

    sort: str
    """
    allow sorting by model name, status, severity or created at, ascending (+) or
    the default descending (-)
    """

    source: Source
    """source of model related to scans"""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start Time"""

    status: List[str]
    """Statuses"""


class ModelName(TypedDict, total=False):
    contains: str

    eq: str


class Source(TypedDict, total=False):
    eq: Literal["adhoc"]
