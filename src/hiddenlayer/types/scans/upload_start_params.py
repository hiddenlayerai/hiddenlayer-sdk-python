# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadStartParams"]


class UploadStartParams(TypedDict, total=False):
    model_name: Required[str]
    """Model name"""

    model_version: Required[str]
    """Model version"""

    requesting_entity: Required[str]
    """Requesting entity"""

    location_alias: str
    """Requested location alias"""
