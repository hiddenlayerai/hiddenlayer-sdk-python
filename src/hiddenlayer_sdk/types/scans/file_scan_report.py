# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["FileScanReport", "Details", "Detection", "DetectionMitreAtlas", "DetectionRuleDetail"]


class Details(BaseModel):
    estimated_time: str
    """estimated time to scan the file"""

    file_type: str
    """type of the file"""

    sha256: str
    """hexadecimal sha256 hash of file"""

    file_size: Optional[str] = None
    """size of the file in human readable format"""

    file_size_bytes: Optional[int] = None
    """size of the file in bytes"""

    file_type_details: Optional[Dict[str, object]] = None

    md5: Optional[str] = None
    """hexadecimal md5 hash of file"""

    tlsh: Optional[str] = None
    """TLSH hash of file"""


class DetectionMitreAtlas(BaseModel):
    tactic: Optional[str] = None
    """MITRE Atlas Tactic"""

    technique: Optional[str] = None
    """MITRE Atlas Technique"""


class DetectionRuleDetail(BaseModel):
    description: Optional[str] = None
    """description of the deprecation"""

    status: Optional[Literal["created", "deprecated", "updated", "superseded"]] = None
    """status"""

    status_at: Optional[datetime] = None
    """date-time when the details entry was created"""


class Detection(BaseModel):
    category: str
    """Vulnerability category for the detection"""

    description: str
    """detection description"""

    detection_id: str
    """unique identifier for the detection"""

    mitre_atlas: List[DetectionMitreAtlas]

    owasp: List[str]

    rule_id: str
    """unique identifier for the rule that sourced the detection"""

    severity: Literal["low", "medium", "high", "critical"]
    """detection severity"""

    cve: Optional[List[str]] = None

    cwe: Optional[str] = None

    cwe_href: Optional[str] = None
    """CWE URL for the detection"""

    impact: Optional[str] = None
    """detection impact"""

    likelihood: Optional[str] = None
    """detection likelihood"""

    risk: Optional[Literal["MALICIOUS", "SUSPICIOUS", "BENIGN"]] = None
    """detection risk"""

    rule_details: Optional[List[DetectionRuleDetail]] = None

    technical_blog_href: Optional[str] = None
    """Hiddenlayer Technical Blog URL for the detection"""


class FileScanReport(BaseModel):
    details: Details

    end_time: datetime
    """time the scan ended"""

    file_instance_id: str
    """unique ID of the file"""

    file_location: str
    """full file path"""

    seen: datetime
    """time the scan was seen at"""

    start_time: datetime
    """time the scan started"""

    status: Literal["skipped", "pending", "running", "done", "failed", "canceled"]
    """status of the scan"""

    detections: Optional[List[Detection]] = None

    file_results: Optional[List["FileScanReport"]] = None


if PYDANTIC_V2:
    FileScanReport.model_rebuild()
    Details.model_rebuild()
    Detection.model_rebuild()
    DetectionMitreAtlas.model_rebuild()
    DetectionRuleDetail.model_rebuild()
else:
    FileScanReport.update_forward_refs()  # type: ignore
    Details.update_forward_refs()  # type: ignore
    Detection.update_forward_refs()  # type: ignore
    DetectionMitreAtlas.update_forward_refs()  # type: ignore
    DetectionRuleDetail.update_forward_refs()  # type: ignore
