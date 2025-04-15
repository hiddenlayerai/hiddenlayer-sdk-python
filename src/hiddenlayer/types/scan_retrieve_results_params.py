# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScanRetrieveResultsParams"]


class ScanRetrieveResultsParams(TypedDict, total=False):
    cursor: str
    """Cursor value returned from a previous request.

    Used to fetch the next page of results.
    """

    page_size: int
