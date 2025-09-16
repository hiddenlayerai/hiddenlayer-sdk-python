# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MetadataProject"]


class MetadataProject(BaseModel):
    project_alias: Optional[str] = None

    project_id: Optional[str] = None

    ruleset_id: Optional[str] = None
