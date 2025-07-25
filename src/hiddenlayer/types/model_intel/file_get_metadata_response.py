# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["FileGetMetadataResponse"]


class FileGetMetadataResponse(BaseModel):
    created_at: datetime
    """Timestamp when the file was created"""

    sha256: str
    """SHA256 hash of the file"""

    size_bytes: int
    """File size in bytes"""

    updated_at: datetime
    """Timestamp when the file was last updated"""

    extension: Optional[str] = None
    """File extension"""

    file_type: Optional[str] = None
    """Type of the file"""

    mime_type: Optional[str] = None
    """MIME type of the file"""
