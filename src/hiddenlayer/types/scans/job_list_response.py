# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .scan_report import ScanReport

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    items: List[ScanReport]
    """List of items. If no matching items are found, then `[]` will be returned."""

    limit: int
    """Maximum number of items to return"""

    offset: int
    """Begin returning the results from this offset"""

    total: float
    """Total number of items available based on the query criteria."""
