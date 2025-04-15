# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelRetrieveResponse", "Version"]


class Version(BaseModel):
    version: str

    locations: Optional[Dict[str, object]] = None

    api_model_version_id: Optional[str] = FieldInfo(alias="model_version_id", default=None)

    multi_file: Optional[bool] = None

    retrievable: Optional[bool] = None

    tags: Optional[Dict[str, object]] = None


class ModelRetrieveResponse(BaseModel):
    name: str

    source: str

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    tenant_id: Optional[str] = None

    versions: Optional[List[Version]] = None
