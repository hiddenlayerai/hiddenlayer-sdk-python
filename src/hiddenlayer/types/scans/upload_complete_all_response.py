# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["UploadCompleteAllResponse"]


class UploadCompleteAllResponse(BaseModel):
    scan_id: str
    """Request to resource is successful"""
