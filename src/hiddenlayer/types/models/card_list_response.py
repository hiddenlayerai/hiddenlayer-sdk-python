# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CardListResponse", "Result", "ResultSecurityPosture"]


class ResultSecurityPosture(BaseModel):
    attack_monitoring: Optional[bool] = None

    api_model_scan: Optional[bool] = FieldInfo(alias="model_scan", default=None)


class Result(BaseModel):
    active_versions: List[int]

    created_at: int
    """Unix Nano Epoch"""

    api_model_id: str = FieldInfo(alias="model_id")

    plaintext_name: str

    source: str

    attack_monitoring_threat_level: Optional[Literal["safe", "unsafe", "suspicious", "not available"]] = None

    api_model_scan_threat_level: Optional[Literal["safe", "unsafe", "suspicious", "not available"]] = FieldInfo(
        alias="model_scan_threat_level", default=None
    )

    security_posture: Optional[ResultSecurityPosture] = None

    tags: Optional[Dict[str, object]] = None


class CardListResponse(BaseModel):
    page_number: int

    page_size: int

    results: List[Result]

    total_count: int
