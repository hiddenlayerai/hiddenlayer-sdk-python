# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V1, ConfigDict
from ..._models import BaseModel

__all__ = [
    "ScanReport",
    "Inventory",
    "InventoryProviderDetails",
    "Summary",
    "Compliance",
    "FileResult",
    "FileResultDetails",
    "FileResultDetailsFileTypeDetails",
    "FileResultDetailsFileTypeDetailsGgufFileAttributes",
    "FileResultDetailsFileTypeDetailsKerasFileAttributes",
    "FileResultDetailsFileTypeDetailsNumpyFileAttributes",
    "FileResultDetailsFileTypeDetailsRdsFileAttributes",
    "FileResultDetection",
    "FileResultDetectionMitreAtlas",
    "FileResultDetectionRuleDetail",
]


class InventoryProviderDetails(BaseModel):
    provider: Literal["AWS_BEDROCK", "AZURE_AI_FOUNDRY", "AWS_SAGEMAKER"]

    provider_model_id: str
    """The provider's unique identifier for the model. Examples:

    - AWS Bedrock: "anthropic.claude-3-5-sonnet-20241022-v2:0"
    - Azure AI Foundry: "Claude-3-5-Sonnet"
    """

    model_arn: Optional[str] = None
    """
    Optional full ARN or resource identifier for the model. Used for provisioned
    models, custom deployments, or cross-account access.
    """

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class Inventory(BaseModel):
    model_id: str
    """Unique identifier for the model"""

    model_name: str
    """name of the model"""

    model_version_id: str
    """unique identifier for the model version"""

    requested_scan_location: str
    """Location to be scanned"""

    asset_region: Optional[str] = None
    """Region of discovered asset"""

    file_location: Optional[str] = None
    """URL or path to the model files, if available"""

    model_source: Optional[str] = None
    """source (provider) info"""

    model_version: Optional[str] = None
    """version of the model"""

    origin: Optional[str] = None
    """
    Specifies the platform or service where the model originated before being
    scanned
    """

    provider_details: Optional[InventoryProviderDetails] = None

    request_source: Optional[
        Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]
    ] = None
    """Identifies the system that requested the scan"""

    requesting_entity: Optional[str] = None
    """Entity that requested the scan"""

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class Summary(BaseModel):
    detection_categories: Optional[List[str]] = None
    """list of unique detection categories found"""

    detection_count: Optional[int] = None
    """total number of detections found"""

    file_count: Optional[int] = None
    """total number of files scanned"""

    files_failed_to_scan: Optional[int] = None
    """number of files that failed during scanning"""

    files_with_detections_count: Optional[int] = None
    """number of files that contain detections"""

    highest_severity: Optional[Literal["critical", "high", "medium", "low", "none", "unknown"]] = None
    """The highest severity of any detections on the scan."""

    severity: Optional[Literal["critical", "high", "medium", "low", "unknown", "safe"]] = None
    """The highest severity of any detections on the scan, including "safe".

    Use `.summary.highest_severity` instead.
    """

    unknown_files: Optional[int] = None
    """number of files with unknown file type"""


class Compliance(BaseModel):
    evaluated_at: Optional[datetime] = None
    """The datetime when the rule set was evaluated against the scan result"""

    rule_set_ids: Optional[List[str]] = None
    """A list of non-default rule sets that were used when evaluating the scan result"""

    status: Optional[Literal["COMPLIANT", "NONCOMPLIANT"]] = None


class FileResultDetailsFileTypeDetailsGgufFileAttributes(BaseModel):
    subtype: List[str]


class FileResultDetailsFileTypeDetailsKerasFileAttributes(BaseModel):
    pickle_modules: List[str]

    subtype: List[str]

    keras_class_name: Optional[str] = None

    keras_date_saved_at: Optional[str] = None

    keras_module: Optional[str] = None

    keras_version: Optional[str] = None
    """version of the Keras file"""


class FileResultDetailsFileTypeDetailsNumpyFileAttributes(BaseModel):
    numpy_arrays: str

    numpy_shape: List[str]

    subtype: List[str]


class FileResultDetailsFileTypeDetailsRdsFileAttributes(BaseModel):
    rds_encoding: str
    """encoding of the RDS file"""

    rds_min_reader_version: str
    """minimum reader version for the RDS file"""

    rds_version: str
    """version of the RDS file"""

    rds_writer_version: str
    """version of the RDS writer"""

    subtype: List[str]


FileResultDetailsFileTypeDetails: TypeAlias = Union[
    FileResultDetailsFileTypeDetailsGgufFileAttributes,
    FileResultDetailsFileTypeDetailsKerasFileAttributes,
    FileResultDetailsFileTypeDetailsNumpyFileAttributes,
    FileResultDetailsFileTypeDetailsRdsFileAttributes,
]


class FileResultDetails(BaseModel):
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

    file_type_details: Optional[FileResultDetailsFileTypeDetails] = None

    md5: Optional[str] = None
    """hexadecimal md5 hash of file"""

    tlsh: Optional[str] = None
    """TLSH hash of file"""


class FileResultDetectionMitreAtlas(BaseModel):
    tactic: Optional[str] = None
    """MITRE Atlas Tactic"""

    technique: Optional[str] = None
    """MITRE Atlas Technique"""


class FileResultDetectionRuleDetail(BaseModel):
    description: Optional[str] = None
    """description of the deprecation"""

    status: Optional[Literal["created", "deprecated", "updated", "superseded"]] = None
    """status"""

    status_at: Optional[datetime] = None
    """date-time when the details entry was created"""


class FileResultDetection(BaseModel):
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

    mitre_atlas: List[FileResultDetectionMitreAtlas]

    owasp: List[str]

    risk: Literal["MALICIOUS", "SUSPICIOUS"]
    """detection risk"""

    rule_id: str
    """unique identifier for the rule that sourced the detection"""

    severity: Literal["critical", "high", "medium", "low"]
    """The severity of the detection."""

    rule_details: Optional[List[FileResultDetectionRuleDetail]] = None

    technical_blog_href: Optional[str] = None
    """Hiddenlayer Technical Blog URL for the detection"""

    technical_blog_hrefs: Optional[List[str]] = None
    """Hiddenlayer Technical Blog URLs for the detection"""


class FileResult(BaseModel):
    details: FileResultDetails

    detections: List[FileResultDetection]

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

    file_error: Optional[List[str]] = None
    """Error messages returned by the scanner"""


class ScanReport(BaseModel):
    """A scan report with all of its details."""

    detection_count: int
    """number of detections found; use `.summary.detection_count` instead"""

    file_count: int
    """number of files scanned; use `.summary.file_count` instead"""

    files_with_detections_count: int
    """
    number of files with detections found; use
    `.summary.files_with_detections_count` instead
    """

    inventory: Inventory

    scan_id: str
    """unique identifier for the scan"""

    start_time: datetime
    """time the scan started"""

    status: Literal["pending", "running", "done", "failed", "canceled"]
    """status of the scan"""

    summary: Summary

    version: str
    """scanner version"""

    schema_version: Optional[str] = FieldInfo(alias="$schema_version", default=None)
    """version of the scan report schema format"""

    compliance: Optional[Compliance] = None

    detection_categories: Optional[List[str]] = None
    """list of detection categories found; use `.summary.detection_categories` instead"""

    end_time: Optional[datetime] = None
    """time the scan ended"""

    file_results: Optional[List[FileResult]] = None

    has_genealogy: Optional[bool] = None
    """if there is model geneaology info available"""

    severity: Optional[Literal["critical", "high", "medium", "low", "unknown", "safe"]] = None
    """The highest severity of any detections on the scan, including "safe".

    Use `.summary.highest_severity` instead.
    """
