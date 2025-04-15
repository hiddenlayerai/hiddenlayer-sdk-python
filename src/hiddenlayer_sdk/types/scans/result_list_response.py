# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["ResultListResponse"]


class ResultListResponse(BaseModel):
    limit: int
    """Maximum number of items to return"""

    offset: int
    """Begin returning the results from this offset"""

    total: int
    """Total number of items available based on the query criteria."""

    items: Optional[List["ScanReport"]] = None
    """List of items. If no matching items are found, then `[]` will be returned."""


from .scan_report import ScanReport

if PYDANTIC_V2:
    ResultListResponse.model_rebuild()
else:
    ResultListResponse.update_forward_refs()  # type: ignore
