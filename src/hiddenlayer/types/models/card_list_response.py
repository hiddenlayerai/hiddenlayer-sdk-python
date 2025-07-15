# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2, ConfigDict
from ..._models import BaseModel

__all__ = ["CardListResponse", "SecurityPosture"]


class SecurityPosture(BaseModel):
    attack_monitoring: Optional[bool] = None

    model_scan: Optional[bool] = None

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class CardListResponse(BaseModel):
    created_at: int
    """Unix Nano Epoch Timestamp"""

    model_id: str

    plaintext_name: str

    source: str

    active_version_count: Optional[int] = None

    attack_monitoring_threat_level: Optional[Literal["safe", "unsafe", "suspicious", "not available"]] = None

    has_genealogy: Optional[bool] = None
    """
    A value of `true` indicates that one or more versions of this model have
    associated model genealogy information.
    """

    model_scan_threat_level: Optional[Literal["safe", "unsafe", "suspicious", "not available"]] = None

    security_posture: Optional[SecurityPosture] = None

    tags: Optional[Dict[str, object]] = None

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())
