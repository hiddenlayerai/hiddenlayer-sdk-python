# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ScanFileResult",
    "Details",
    "DetailsFileTypeDetails",
    "DetailsFileTypeDetailsGgufFileAttributes",
    "DetailsFileTypeDetailsKerasFileAttributes",
    "DetailsFileTypeDetailsNumpyFileAttributes",
    "DetailsFileTypeDetailsRdsFileAttributes",
    "Detection",
    "DetectionMitreAtlas",
    "DetectionRuleDetail",
    "Advisory",
    "Compliance",
]


class DetailsFileTypeDetailsGgufFileAttributes(BaseModel):
    subtype: List[str]


class DetailsFileTypeDetailsKerasFileAttributes(BaseModel):
    pickle_modules: List[str]

    subtype: List[str]

    keras_class_name: Optional[str] = None

    keras_date_saved_at: Optional[str] = None

    keras_module: Optional[str] = None

    keras_version: Optional[str] = None
    """version of the Keras file"""


class DetailsFileTypeDetailsNumpyFileAttributes(BaseModel):
    numpy_arrays: str

    numpy_shape: List[str]

    subtype: List[str]


class DetailsFileTypeDetailsRdsFileAttributes(BaseModel):
    rds_encoding: str
    """encoding of the RDS file"""

    rds_min_reader_version: str
    """minimum reader version for the RDS file"""

    rds_version: str
    """version of the RDS file"""

    rds_writer_version: str
    """version of the RDS writer"""

    subtype: List[str]


DetailsFileTypeDetails: TypeAlias = Union[
    DetailsFileTypeDetailsGgufFileAttributes,
    DetailsFileTypeDetailsKerasFileAttributes,
    DetailsFileTypeDetailsNumpyFileAttributes,
    DetailsFileTypeDetailsRdsFileAttributes,
]


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

    file_type_details: Optional[DetailsFileTypeDetails] = None

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

    cve: List[str]

    cwe: str

    cwe_href: str
    """CWE URL for the detection"""

    description: str
    """detection description"""

    detection_id: str
    """unique identifier for the detection"""

    impact: str
    """detection impact"""

    likelihood: str
    """detection likelihood"""

    mitre_atlas: List[DetectionMitreAtlas]

    owasp: List[str]

    risk: Literal["MALICIOUS", "SUSPICIOUS"]
    """detection risk"""

    rule_id: str
    """unique identifier for the rule that sourced the detection"""

    severity: Literal["critical", "high", "medium", "low"]
    """The severity of the detection."""

    rule_details: Optional[List[DetectionRuleDetail]] = None

    technical_blog_href: Optional[str] = None
    """Hiddenlayer Technical Blog URL for the detection"""

    technical_blog_hrefs: Optional[List[str]] = None
    """Hiddenlayer Technical Blog URLs for the detection"""


class Advisory(BaseModel):
    """An informational advisory associated with a file.

    Advisories carry guidance about
    a property of the model (e.g. tokenizer family) that may matter to a downstream
    consumer, but do not represent a concrete detection.
    """

    advisory_id: str
    """unique identifier for the advisory"""

    category: str
    """category for the advisory"""

    description: str
    """advisory description"""

    rule_id: str
    """unique identifier for the rule that sourced the advisory"""


class Compliance(BaseModel):
    rationale: Optional[List[str]] = None

    status: Optional[Literal["COMPLIANT", "NONCOMPLIANT"]] = None


class ScanFileResult(BaseModel):
    details: Details

    detections: List[Detection]

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

    advisories: Optional[List[Advisory]] = None
    """informational advisories associated with this file (e.g. tokenizer family)"""

    compliance: Optional[Compliance] = None

    file_error: Optional[List[str]] = None
    """Error messages returned by the scanner"""
