# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V1, ConfigDict
from ..._models import BaseModel

__all__ = [
    "ScanJob",
    "Inventory",
    "InventoryScanTarget",
    "InventoryScanTargetDeepScan",
    "InventoryScanTargetDeepScanFile",
    "InventoryScanTargetProviderDetails",
]


class InventoryScanTargetDeepScanFile(BaseModel):
    file_location: str
    """URL or path to the specific file"""

    file_name_alias: Optional[str] = None
    """Optional alias for the file name"""


class InventoryScanTargetDeepScan(BaseModel):
    file_location: Optional[str] = None
    """URL or path to the model files"""

    files: Optional[List[InventoryScanTargetDeepScanFile]] = None
    """List of specific files to scan"""


class InventoryScanTargetProviderDetails(BaseModel):
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


class InventoryScanTarget(BaseModel):
    """Specifies what to scan.

    Must provide at least one of:
    deep_scan with file location details, provider_details, or both.
    """

    asset_region: Optional[str] = None
    """region of the discovered asset"""

    deep_scan: Optional[InventoryScanTargetDeepScan] = None

    provider_details: Optional[InventoryScanTargetProviderDetails] = None


class Inventory(BaseModel):
    model_name: str
    """Name of the model"""

    model_version: str
    """If you do not provide a version, one will be generated for you."""

    requesting_entity: str
    """Entity that requested the scan"""

    origin: Optional[str] = None
    """
    Specifies the platform or service where the model originated before being
    scanned
    """

    request_source: Optional[
        Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]
    ] = None
    """Identifies the system that requested the scan"""

    requested_scan_location: Optional[str] = None
    """**DEPRECATED**: Use `scan_target` instead. Location of files to be scanned.

    Maintained for backwards compatibility. If both `requested_scan_location` and
    `scan_target` are provided, `scan_target` takes precedence.
    """

    scan_target: Optional[InventoryScanTarget] = None
    """Specifies what to scan.

    Must provide at least one of: deep_scan with file location details,
    provider_details, or both.
    """

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ScanJob(BaseModel):
    inventory: Inventory

    scan_id: Optional[str] = None
    """unique identifier for the scan"""

    status: Optional[Literal["pending", "running", "done", "failed", "canceled"]] = None
    """Status of the scan"""
