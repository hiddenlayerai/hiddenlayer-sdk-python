# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CardListParams", "ModelCreated", "ModelName", "Source"]


class CardListParams(TypedDict, total=False):
    aidr_severity: List[Literal["SAFE", "UNSAFE", "SUSPICIOUS"]]

    aidr_status: Literal["ENABLED", "DISABLED", "ANY"]
    """filter by aidr enabled"""

    limit: int
    """Limit the number of items returned"""

    model_created: ModelCreated
    """match on models created between dates"""

    model_name: ModelName
    """substring match on model name"""

    modscan_severity: List[Literal["SAFE", "UNSAFE", "SUSPICIOUS", "UNKNOWN", "ERROR"]]

    modscan_status: Literal["ENABLED", "DISABLED", "ANY"]

    offset: int
    """Begin returning the results from this offset"""

    provider: List[Literal["AZURE", "ADHOC"]]

    sort: str
    """
    allow sorting by model name or created at timestamp, ascending (+) or the
    default descending (-)
    """

    source: Source
    """substring and full match on model source"""

    x_correlation_id: Annotated[str, PropertyInfo(alias="X-Correlation-Id")]


class ModelCreated(TypedDict, total=False):
    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class ModelName(TypedDict, total=False):
    contains: str

    eq: str


class Source(TypedDict, total=False):
    contains: str

    eq: str
