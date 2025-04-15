# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["VectorSubmitVectorsParams"]


class VectorSubmitVectorsParams(TypedDict, total=False):
    input_layer: Required[str]

    input_layer_dtype: Required[str]

    input_layer_shape: Required[Iterable[float]]

    output_layer: Required[str]

    output_layer_dtype: Required[str]

    output_layer_shape: Required[Iterable[float]]

    sensor_id: Required[str]

    event_time: str

    metadata: object

    predictions: Iterable[float]

    requester_id: str

    tags: List[str]
