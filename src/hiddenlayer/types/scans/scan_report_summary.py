# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V1, ConfigDict
from ..._models import BaseModel

__all__ = [
    "ScanReportSummary",
    "Inventory",
    "InventoryProviderDetails",
    "Summary",
    "SummaryMitreAtlas",
    "Compliance",
    "Intelligence",
    "IntelligenceLicense",
    "IntelligenceUsagePolicy",
]


class InventoryProviderDetails(BaseModel):
    provider: Literal["AWS_BEDROCK", "AWS_SAGEMAKER", "AZURE_AI_FOUNDRY", "AZURE_ML", "DATABRICKS"]

    provider_model_id: str
    """The provider's unique identifier for the model. Examples:

    - AWS Bedrock: "anthropic.claude-3-5-sonnet-20241022-v2:0"
    - Azure AI Foundry: "Claude-3-5-Sonnet"
    """

    country: Optional[str] = None
    """
    Optional country code (ISO 3166-1 alpha-2) for the location where the model
    provider is primarily based.
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

    asset_id: Optional[str] = None
    """Identifier of discovered asset"""

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


class SummaryMitreAtlas(BaseModel):
    tactic: Optional[str] = None
    """MITRE Atlas Tactic"""

    technique: Optional[str] = None
    """MITRE Atlas Technique"""


class Summary(BaseModel):
    advisory_categories: Optional[List[str]] = None
    """list of unique advisory categories found"""

    advisory_count: Optional[int] = None
    """total number of advisories found"""

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

    mitre_atlas: Optional[List[SummaryMitreAtlas]] = None
    """
    deduped list of MITRE Atlas tactic/technique pairs across all detections in the
    scan
    """

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


class IntelligenceLicense(BaseModel):
    """License information for a model"""

    name: str
    """Name of the license"""

    sha256: str
    """SHA256 hash of the license file"""


class IntelligenceUsagePolicy(BaseModel):
    """Usage policy information for a model"""

    name: str
    """Name of the usage policy"""

    sha256: str
    """SHA256 hash of the policy document"""


class Intelligence(BaseModel):
    """
    Intelligence metadata about a model including origin, licensing, and usage policies
    """

    contributor_trust_level: Optional[str] = None
    """Trust level of the model contributor"""

    country_of_origin: Optional[str] = None
    """ISO 3166-1 alpha-2 country code of the model's primary origin"""

    geographic_footprint: Optional[List[str]] = None
    """List of countries where the model originated"""

    licenses: Optional[List[IntelligenceLicense]] = None
    """List of licenses associated with the model"""

    usage_policies: Optional[List[IntelligenceUsagePolicy]] = None
    """List of usage policies associated with the model"""


class ScanReportSummary(BaseModel):
    """
    A scan report summary containing header and aggregated statistics without file-level results.
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

    end_time: Optional[datetime] = None
    """time the scan ended"""

    has_genealogy: Optional[bool] = None
    """if there is model geneaology info available"""

    intelligence: Optional[Intelligence] = None
    """
    Intelligence metadata about a model including origin, licensing, and usage
    policies
    """

    referenced_models: Optional[List[str]] = None
    """URLs of model artifact files referenced in a NIM container's
    model_manifest.yaml.

    Only present for NIM container scans.
    """

    scan_error: Optional[List[str]] = None
    """Error messages returned by the scanner"""
