# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileScanReportParam", "Details", "Detection", "DetectionMitreAtlas", "DetectionRuleDetail"]


class Details(TypedDict, total=False):
    estimated_time: Required[str]
    """estimated time to scan the file"""

    file_type: Required[str]
    """type of the file"""

    sha256: Required[str]
    """hexadecimal sha256 hash of file"""

    file_size: str
    """size of the file in human readable format"""

    file_size_bytes: int
    """size of the file in bytes"""

    file_type_details: Dict[str, object]

    md5: str
    """hexadecimal md5 hash of file"""

    tlsh: str
    """TLSH hash of file"""


class DetectionMitreAtlas(TypedDict, total=False):
    tactic: str
    """MITRE Atlas Tactic"""

    technique: str
    """MITRE Atlas Technique"""


class DetectionRuleDetail(TypedDict, total=False):
    description: str
    """description of the deprecation"""

    status: Literal["created", "deprecated", "updated", "superseded"]
    """status"""

    status_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """date-time when the details entry was created"""


class Detection(TypedDict, total=False):
    category: Required[str]
    """Vulnerability category for the detection"""

    description: Required[str]
    """detection description"""

    detection_id: Required[str]
    """unique identifier for the detection"""

    mitre_atlas: Required[Iterable[DetectionMitreAtlas]]

    owasp: Required[List[str]]

    rule_id: Required[str]
    """unique identifier for the rule that sourced the detection"""

    severity: Required[Literal["low", "medium", "high", "critical"]]
    """detection severity"""

    cve: List[str]

    cwe: str

    cwe_href: str
    """CWE URL for the detection"""

    impact: str
    """detection impact"""

    likelihood: str
    """detection likelihood"""

    risk: Literal["MALICIOUS", "SUSPICIOUS", "BENIGN"]
    """detection risk"""

    rule_details: Iterable[DetectionRuleDetail]

    technical_blog_href: str
    """Hiddenlayer Technical Blog URL for the detection"""


class FileScanReportParam(TypedDict, total=False):
    details: Required[Details]

    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """time the scan ended"""

    file_instance_id: Required[str]
    """unique ID of the file"""

    file_location: Required[str]
    """full file path"""

    seen: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """time the scan was seen at"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """time the scan started"""

    status: Required[Literal["skipped", "pending", "running", "done", "failed", "canceled"]]
    """status of the scan"""

    detections: Iterable[Detection]

    file_results: Iterable["FileScanReportParam"]
