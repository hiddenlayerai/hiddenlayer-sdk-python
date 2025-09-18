# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromptAnalyzerCreateParams"]


class PromptAnalyzerCreateParams(TypedDict, total=False):
    prompt: Required[str]

    model: str

    output: str

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]

    x_requester_id: Annotated[str, PropertyInfo(alias="X-Requester-Id")]
