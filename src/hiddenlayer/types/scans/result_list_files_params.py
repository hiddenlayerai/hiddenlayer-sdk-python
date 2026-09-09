# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResultListFilesParams"]


class ResultListFilesParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination, used to navigate through pages of results"""

    has_detections: bool
    """When true, only return files that have detections"""

    page_size: int
    """Number of items to return per page"""
