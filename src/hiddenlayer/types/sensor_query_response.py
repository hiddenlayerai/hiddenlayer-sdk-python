# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .sensor import Sensor
from .._models import BaseModel

__all__ = ["SensorQueryResponse"]


class SensorQueryResponse(BaseModel):
    page_number: int

    page_size: int

    results: List[Sensor]

    total_count: int
