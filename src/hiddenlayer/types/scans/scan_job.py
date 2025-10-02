# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V1, ConfigDict
from ..._models import BaseModel

__all__ = ["ScanJob", "Inventory"]


class Inventory(BaseModel):
    model_name: str
    """Name of the model"""

    model_version: str
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

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ScanJob(BaseModel):
    inventory: Inventory

    scan_id: Optional[str] = None
    """unique identifier for the scan"""

    status: Optional[Literal["pending", "running", "done", "failed", "canceled"]] = None
    """Status of the scan"""
