# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScanJob", "Inventory"]


class Inventory(BaseModel):
    api_model_name: str = FieldInfo(alias="model_name")
    """Name of the model"""

    api_model_version: str = FieldInfo(alias="model_version")
    """If you do not provide a version, one will be generated for you."""

    requested_scan_location: str
    """Location to be scanned"""

    requesting_entity: str
    """Entity that requested the scan"""

    origin: Optional[str] = None
    """
    Specifies the platform or service where the model originated before being
    scanned
    """

    request_source: Optional[Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload"]] = None
    """Identifies the system that requested the scan"""


class ScanJob(BaseModel):
    inventory: Inventory

    scan_id: Optional[str] = None
    """unique identifier for the scan"""

    status: Optional[Literal["pending", "running", "done", "failed", "canceled"]] = None
    """Status of the scan"""
