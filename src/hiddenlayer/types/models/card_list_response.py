# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["CardListResponse", "Result"]


class Result:
    pass


class CardListResponse(BaseModel):
    page_number: int

    page_size: int

    results: List[Result]

    total_count: int
