# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["FileCompleteResponse"]


class FileCompleteResponse(BaseModel):
    scan_id: Optional[str] = None
    """Request to resource is successful"""
