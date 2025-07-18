# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ModelCreateParams", "Body", "BodyVersion", "BodyVersionDeployment"]


class ModelCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyVersionDeployment(TypedDict, total=False):
    active: bool

    path: str


class BodyVersion(TypedDict, total=False):
    version: Required[str]

    deployments: Iterable[BodyVersionDeployment]

    locations: Dict[str, object]

    model_version_id: str

    multi_file: bool

    retrievable: bool

    tags: Dict[str, object]


class Body(TypedDict, total=False):
    name: Required[str]

    source: Required[str]

    model_id: str

    tenant_id: str

    versions: Iterable[BodyVersion]
