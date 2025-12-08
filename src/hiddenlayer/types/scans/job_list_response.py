# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V1, ConfigDict
from ..._models import BaseModel

__all__ = ["JobListResponse", "Item", "ItemInventory", "ItemInventoryProviderDetails", "ItemSummary", "ItemCompliance"]


class ItemInventoryProviderDetails(BaseModel):
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


class ItemInventory(BaseModel):
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

    provider_details: Optional[ItemInventoryProviderDetails] = None

    request_source: Optional[
        Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]
    ] = None
    """Identifies the system that requested the scan"""

    requesting_entity: Optional[str] = None
    """Entity that requested the scan"""

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ItemSummary(BaseModel):
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


class ItemCompliance(BaseModel):
    evaluated_at: Optional[datetime] = None
    """The datetime when the rule set was evaluated against the scan result"""

    rule_set_ids: Optional[List[str]] = None
    """A list of non-default rule sets that were used when evaluating the scan result"""

    status: Optional[Literal["COMPLIANT", "NONCOMPLIANT"]] = None


class Item(BaseModel):
    """A scan report without any file results."""

    detection_count: int
    """number of detections found; use `.summary.detection_count` instead"""

    file_count: int
    """number of files scanned; use `.summary.file_count` instead"""

    files_with_detections_count: int
    """
    number of files with detections found; use
    `.summary.files_with_detections_count` instead
    """

    inventory: ItemInventory

    scan_id: str
    """unique identifier for the scan"""

    start_time: datetime
    """time the scan started"""

    status: Literal["pending", "running", "done", "failed", "canceled"]
    """status of the scan"""

    summary: ItemSummary

    version: str
    """scanner version"""

    schema_version: Optional[str] = FieldInfo(alias="$schema_version", default=None)
    """version of the scan report schema format"""

    compliance: Optional[ItemCompliance] = None

    detection_categories: Optional[List[str]] = None
    """list of detection categories found; use `.summary.detection_categories` instead"""

    end_time: Optional[datetime] = None
    """time the scan ended"""

    has_genealogy: Optional[bool] = None
    """if there is model geneaology info available"""

    severity: Optional[Literal["critical", "high", "medium", "low", "unknown", "safe"]] = None
    """The highest severity of any detections on the scan, including "safe".

    Use `.summary.highest_severity` instead.
    """


class JobListResponse(BaseModel):
    items: List[Item]
    """List of items. If no matching items are found, then `[]` will be returned."""

    limit: int
    """Maximum number of items to return"""

    offset: int
    """Begin returning the results from this offset"""

    total: float
    """Total number of items available based on the query criteria."""
