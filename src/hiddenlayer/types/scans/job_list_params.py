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

    deep_scan: bool
    """When true, returns only scans that with files.

    When false, returns only scans without files. When not provided, returns all
    scans.
    """

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

    provider: SequenceNotStr[str]
    """Filter by model provider name"""

    region: SequenceNotStr[str]
    """Filter by region of the discovered asset"""

    request_source: List[Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]]
    """Filter by request source using a comma-separated list"""

    scanner_version: str
    """filter by version of the scanner"""

    severity: Literal["critical", "high", "medium", "low", "none", "unknown", "safe"]
    """Severities"""

    sort: str
    """
    allow sorting by model name, status, severity, scan start time, asset region, or
    model provider ascending (+) or the default descending (-)
    """

    source: Source
    """source of model related to scans"""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start Time"""

    status: SequenceNotStr[str]
    """Statuses"""


class ModelName(TypedDict, total=False):
    """filter by the model name"""

    contains: str

    eq: str


class Source(TypedDict, total=False):
    """source of model related to scans"""

    eq: Literal["adhoc"]
