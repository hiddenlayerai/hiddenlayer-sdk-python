# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["FileAddResponse", "Part"]


class Part(BaseModel):
    end_offset: Optional[int] = None

    part_number: Optional[int] = None

    start_offset: Optional[int] = None

    upload_url: Optional[str] = None


class FileAddResponse(BaseModel):
    parts: List[Part]

    upload_id: str
    """UploadId for the current file"""
