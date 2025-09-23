# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["JobListParams", "ModelName", "Source"]


class JobListParams(TypedDict, total=False):
    compliance_status: List[Literal["COMPLIANT", "NONCOMPLIANT"]]
    """A comma separated list of rule set evaluation statuses to include"""

    detection_category: str
    """filter by a single detection category"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End Time"""

    latest_per_model_version_only: bool
    """only return latest result per model version"""

    limit: int

    model_ids: SequenceNotStr[str]
    """Model ID"""

    model_name: ModelName
    """filter by the model name"""

    model_version_ids: SequenceNotStr[str]
    """Model Version IDs"""

    offset: int

    request_source: List[Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload"]]
    """Filter by request source using a comma-separated list"""

    scanner_version: str
    """filter by version of the scanner"""

    severity: SequenceNotStr[str]
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

    status: SequenceNotStr[str]
    """Statuses"""

    x_correlation_id: Annotated[str, PropertyInfo(alias="X-Correlation-Id")]


class ModelName(TypedDict, total=False):
    contains: str

    eq: str


class Source(TypedDict, total=False):
    eq: Literal["adhoc"]
