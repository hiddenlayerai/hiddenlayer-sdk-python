# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Sensor"]


class Sensor(BaseModel):
    active: bool

    created_at: datetime

    plaintext_name: str

    sensor_id: str

    tenant_id: str

    version: int

    tags: Optional[Dict[str, object]] = None
