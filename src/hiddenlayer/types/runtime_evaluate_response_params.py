# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RuntimeEvaluateResponseParams"]


class RuntimeEvaluateResponseParams(TypedDict, total=False):
    body: Required[Dict[str, object]]
    """A pass-through payload in the native format of the LLM provider.

    Any valid provider request or response payload is accepted as-is and returned in
    the same format.
    """

    hl_project_id: Annotated[str, PropertyInfo(alias="HL-Project-Id")]

    hl_runtime_session_id: Annotated[str, PropertyInfo(alias="HL-Runtime-Session-Id")]
