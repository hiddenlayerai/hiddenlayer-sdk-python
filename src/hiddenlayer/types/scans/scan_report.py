# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["ScanReport", "Inventory"]


class Inventory(BaseModel):
    api_model_id: str = FieldInfo(alias="model_id")
    """Unique identifier for the model"""

    api_model_name: str = FieldInfo(alias="model_name")
    """name of the model"""

    api_model_version: str = FieldInfo(alias="model_version")
    """version of the model"""

    api_model_version_id: str = FieldInfo(alias="model_version_id")
    """unique identifier for the model version"""

    requested_scan_location: str
    """Location to be scanned"""

    api_model_source: Optional[str] = FieldInfo(alias="model_source", default=None)
    """source (provider) info"""

    requesting_entity: Optional[str] = None
    """Entity that requested the scan"""


class ScanReport(BaseModel):
    detection_count: int
    """number of detections found"""

    file_count: int
    """number of files scanned"""

    files_with_detections_count: int
    """number of files with detections found"""

    inventory: Inventory
    """information about model and version that this scan relates to"""

    scan_id: str
    """unique identifier for the scan"""

    start_time: datetime
    """time the scan started"""

    status: Literal["pending", "running", "done", "failed", "canceled"]
    """status of the scan"""

    version: str
    """scanner version"""

    detection_categories: Optional[List[str]] = None
    """list of detection categories found"""

    end_time: Optional[datetime] = None
    """time the scan ended"""

    file_results: Optional[List["FileScanReport"]] = None

    severity: Optional[Literal["low", "medium", "high", "critical", "safe", "unknown"]] = None
    """detection severity"""


from .file_scan_report import FileScanReport

if PYDANTIC_V2:
    ScanReport.model_rebuild()
    Inventory.model_rebuild()
else:
    ScanReport.update_forward_refs()  # type: ignore
    Inventory.update_forward_refs()  # type: ignore
