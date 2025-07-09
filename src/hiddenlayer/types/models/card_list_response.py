# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2, ConfigDict
from ..._models import BaseModel

__all__ = ["CardListResponse", "Result", "ResultSecurityPosture"]


class ResultSecurityPosture(BaseModel):
    attack_monitoring: Optional[bool] = None

    model_scan: Optional[bool] = None

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class Result(BaseModel):
    created_at: int
    """Unix Nano Epoch Timestamp"""

    model_id: str

    plaintext_name: str

    source: str

    active_versions: Optional[List[int]] = None

    attack_monitoring_threat_level: Optional[Literal["safe", "unsafe", "suspicious", "not available"]] = None

    model_scan_threat_level: Optional[Literal["safe", "unsafe", "suspicious", "not available"]] = None

    security_posture: Optional[ResultSecurityPosture] = None

    tags: Optional[Dict[str, object]] = None

    if PYDANTIC_V2:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class CardListResponse(BaseModel):
    page_number: int

    page_size: int

    results: List[Result]

    total_count: int
