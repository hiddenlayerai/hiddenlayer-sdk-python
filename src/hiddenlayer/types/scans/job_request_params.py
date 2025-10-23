# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobRequestParams", "Access", "Inventory", "InventoryScanTarget", "InventoryScanTargetProviderModel"]


class JobRequestParams(TypedDict, total=False):
    access: Required[Access]
    """Access method for the location of files associated with the scan"""

    inventory: Required[Inventory]


class Access(TypedDict, total=False):
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


class InventoryScanTargetProviderModel(TypedDict, total=False):
    model_id: Required[str]
    """The provider's unique identifier for the model. Examples:

    - AWS Bedrock: "anthropic.claude-3-5-sonnet-20241022-v2:0"
    - Azure AI Foundry: "Claude-3-5-Sonnet"
    """

    provider: Required[Literal["AWS_BEDROCK", "AZURE_AI_FOUNDRY", "AWS_SAGEMAKER"]]

    model_arn: str
    """
    Optional full ARN or resource identifier for the model. Used for provisioned
    models, custom deployments, or cross-account access.
    """


class InventoryScanTarget(TypedDict, total=False):
    file_location: str
    """URL or path to the model files"""

    provider_model: InventoryScanTargetProviderModel


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

    Must provide at least one of: file_location, provider_model, or both.
    """
