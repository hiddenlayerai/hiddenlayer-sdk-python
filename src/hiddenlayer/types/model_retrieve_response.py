# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._compat import PYDANTIC_V1, ConfigDict
from .._models import BaseModel

__all__ = ["ModelRetrieveResponse", "Version", "VersionDeployment"]


class VersionDeployment(BaseModel):
    active: Optional[bool] = None

    path: Optional[str] = None


class Version(BaseModel):
    version: str

    deployments: Optional[List[VersionDeployment]] = None

    locations: Optional[Dict[str, object]] = None

    model_version_id: Optional[str] = None

    multi_file: Optional[bool] = None

    retrievable: Optional[bool] = None

    tags: Optional[Dict[str, object]] = None

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class ModelRetrieveResponse(BaseModel):
    name: str

    source: str

    model_id: Optional[str] = None

    tenant_id: Optional[str] = None

    versions: Optional[List[Version]] = None

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())
