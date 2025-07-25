# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FileRetrieveParams"]


class FileRetrieveParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination, used to navigate through pages of results"""

    page_size: int
    """Number of items to return per page"""
