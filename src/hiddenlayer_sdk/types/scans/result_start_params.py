# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResultStartParams", "Inventory"]


class ResultStartParams(TypedDict, total=False):
    detection_count: Required[int]
    """number of detections found"""

    file_count: Required[int]
    """number of files scanned"""

    files_with_detections_count: Required[int]
    """number of files with detections found"""

    inventory: Required[Inventory]
    """information about model and version that this scan relates to"""

    body_scan_id: Required[Annotated[str, PropertyInfo(alias="scan_id")]]
    """unique identifier for the scan"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """time the scan started"""

    status: Required[Literal["pending", "running", "done", "failed", "canceled"]]
    """status of the scan"""

    version: Required[str]
    """scanner version"""

    has_detections: bool
    """Filter file_results to only those that have detections (and parents)"""

    detection_categories: List[str]
    """list of detection categories found"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """time the scan ended"""

    file_results: Iterable["FileScanReportParam"]

    severity: Literal["low", "medium", "high", "critical", "safe", "unknown"]
    """detection severity"""


class Inventory(TypedDict, total=False):
    model_id: Required[str]
    """Unique identifier for the model"""

    model_name: Required[str]
    """name of the model"""

    model_version: Required[str]
    """version of the model"""

    model_version_id: Required[str]
    """unique identifier for the model version"""

    requested_scan_location: Required[str]
    """Location to be scanned"""

    model_source: str
    """source (provider) info"""

    requesting_entity: str
    """Entity that requested the scan"""


from .file_scan_report_param import FileScanReportParam
