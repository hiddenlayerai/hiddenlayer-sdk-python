# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._compat import PYDANTIC_V1, ConfigDict
from .._models import BaseModel

__all__ = ["SensorQueryResponse", "Result"]


class Result(BaseModel):
    active: bool

    created_at: datetime

    model_id: str

    plaintext_name: str

    sensor_id: str

    tags: Dict[str, object]

    tenant_id: str

    adhoc: Optional[bool] = None

    version: Optional[int] = None

    if not PYDANTIC_V1:
        # allow fields with a `model_` prefix
        model_config = ConfigDict(protected_namespaces=tuple())


class SensorQueryResponse(BaseModel):
    page_number: int

    page_size: int

    results: List[Result]

    total_count: int
