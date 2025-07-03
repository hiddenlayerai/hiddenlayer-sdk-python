# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobRequestParams", "Access", "Inventory"]


class JobRequestParams(TypedDict, total=False):
    access: Required[Access]

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
    ]


class Inventory(TypedDict, total=False):
    model_name: Required[str]
    """Name of the model"""

    model_version: Required[str]
    """If you do not provide a version, one will be generated for you."""

    requested_scan_location: Required[str]
    """Location to be scanned"""

    requesting_entity: Required[str]
    """Entity that requested the scan"""

    origin: str
    """
    Specifies the platform or service where the model originated before being
    scanned
    """

    request_source: Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload"]
    """Identifies the system that requested the scan"""
