# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResultListParams"]


class ResultListParams(TypedDict, total=False):
    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End Time"""

    latest_per_model_version_only: bool
    """only return latest result per model version"""

    limit: int

    model_ids: List[str]
    """Model ID"""

    model_version_ids: List[str]
    """Model Version ID"""

    offset: int

    severity: List[str]
    """Severities"""

    sort: str
    """
    allow sorting by status, severity or created at, ascending (+) or the default
    descending (-)
    """

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start Time"""

    status: List[str]
    """Statuses"""
