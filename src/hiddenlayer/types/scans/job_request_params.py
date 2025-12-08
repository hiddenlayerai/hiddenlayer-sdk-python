# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "JobRequestParams",
    "Access",
    "Inventory",
    "InventoryScanTarget",
    "InventoryScanTargetDeepScan",
    "InventoryScanTargetDeepScanFile",
    "InventoryScanTargetProviderDetails",
]


class JobRequestParams(TypedDict, total=False):
    access: Required[Access]
    """Access method for the location of files associated with the scan"""

    inventory: Required[Inventory]


class Access(TypedDict, total=False):
    """Access method for the location of files associated with the scan"""

    source: Literal[
        "LOCAL",
        "AWS_PRESIGNED",
        "AWS_IAM_ROLE",
        "AZURE_BLOB_SAS",
        "AZURE_BLOB_AD",
        "GOOGLE_SIGNED",
        "GOOGLE_OAUTH",
        "HUGGING_FACE",
        "NONE",
    ]


class InventoryScanTargetDeepScanFile(TypedDict, total=False):
    file_location: Required[str]
    """URL or path to the specific file"""

    file_name_alias: str
    """Optional alias for the file name"""


class InventoryScanTargetDeepScan(TypedDict, total=False):
    file_location: str
    """URL or path to the model files"""

    files: Iterable[InventoryScanTargetDeepScanFile]
    """List of specific files to scan"""


class InventoryScanTargetProviderDetails(TypedDict, total=False):
    provider: Required[Literal["AWS_BEDROCK", "AZURE_AI_FOUNDRY", "AWS_SAGEMAKER"]]

    provider_model_id: Required[str]
    """The provider's unique identifier for the model. Examples:

    - AWS Bedrock: "anthropic.claude-3-5-sonnet-20241022-v2:0"
    - Azure AI Foundry: "Claude-3-5-Sonnet"
    """

    model_arn: str
    """
    Optional full ARN or resource identifier for the model. Used for provisioned
    models, custom deployments, or cross-account access.
    """


class InventoryScanTarget(TypedDict, total=False):
    """Specifies what to scan.

    Must provide at least one of:
    deep_scan with file location details, provider_details, or both.
    """

    asset_region: str
    """region of the discovered asset"""

    deep_scan: InventoryScanTargetDeepScan

    provider_details: InventoryScanTargetProviderDetails


class Inventory(TypedDict, total=False):
    model_name: Required[str]
    """Name of the model"""

    model_version: Required[str]
    """If you do not provide a version, one will be generated for you."""

    requesting_entity: Required[str]
    """Entity that requested the scan"""

    origin: str
    """
    Specifies the platform or service where the model originated before being
    scanned
    """

    request_source: Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]
    """Identifies the system that requested the scan"""

    requested_scan_location: str
    """**DEPRECATED**: Use `scan_target` instead. Location of files to be scanned.

    Maintained for backwards compatibility. If both `requested_scan_location` and
    `scan_target` are provided, `scan_target` takes precedence.
    """

    scan_target: InventoryScanTarget
    """Specifies what to scan.

    Must provide at least one of: deep_scan with file location details,
    provider_details, or both.
    """
