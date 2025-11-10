# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V1, ConfigDict
from ..._models import BaseModel

__all__ = ["CardListResponse", "SecurityPosture"]


class SecurityPosture(BaseModel):
    attack_monitoring: Optional[bool] = None

    model_scan: Optional[bool] = None

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class CardListResponse(BaseModel):
    active_version_count: int

    attack_monitoring_threat_level: Literal["safe", "unsafe", "suspicious", "not available"]

    created_at: int
    """Unix Nano Epoch Timestamp"""

    has_genealogy: bool
    """
    A value of `true` indicates that one or more versions of this model have
    associated model genealogy information.
    """

    model_id: str

    model_scan_severity: Literal["not available", "critical", "high", "medium", "low", "none", "unknown"]
    """The severity of the model's latest scan"""

    model_scan_threat_level: Literal["safe", "unsafe", "suspicious", "not available"]

    plaintext_name: str

    source: str

    aidr_threat_level: Optional[Literal["high", "medium", "low", "none", "not available"]] = None

    model_scan_has_error: Optional[bool] = None
    """True if the model's latest scan has an error"""

    security_posture: Optional[SecurityPosture] = None

    tags: Optional[Dict[str, object]] = None

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())
