# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JobRetrieveParams"]


class JobRetrieveParams(TypedDict, total=False):
    has_detections: bool
    """Filter file_results to only those that have detections (and parents)"""
