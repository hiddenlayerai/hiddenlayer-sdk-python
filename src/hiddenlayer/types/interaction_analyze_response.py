# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "InteractionAnalyzeResponse",
    "Analysis",
    "AnalysisFindings",
    "AnalysisFindingsFramework",
    "AnalyzedData",
    "AnalyzedDataInput",
    "AnalyzedDataInputMessage",
    "AnalyzedDataOutput",
    "AnalyzedDataOutputMessage",
    "Metadata",
    "MetadataProject",
    "ModifiedData",
    "ModifiedDataInput",
    "ModifiedDataInputMessage",
    "ModifiedDataOutput",
    "ModifiedDataOutputMessage",
]


class AnalysisFindingsFramework(BaseModel):
    label: str

    name: str


class AnalysisFindings(BaseModel):
    frameworks: Dict[str, List[AnalysisFindingsFramework]]

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Analysis(BaseModel):
    id: str

    configuration: Dict[str, object]

    detected: bool

    findings: AnalysisFindings

    name: str

    phase: str

    processing_time_ms: float

    version: str


class AnalyzedDataInputMessage(BaseModel):
    content: str

    role: Optional[str] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AnalyzedDataInput(BaseModel):
    messages: Optional[List[AnalyzedDataInputMessage]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AnalyzedDataOutputMessage(BaseModel):
    content: str

    role: Optional[str] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AnalyzedDataOutput(BaseModel):
    messages: Optional[List[AnalyzedDataOutputMessage]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AnalyzedData(BaseModel):
    input: AnalyzedDataInput

    output: Optional[AnalyzedDataOutput] = None


class MetadataProject(BaseModel):
    project_alias: Optional[str] = None

    project_id: Optional[str] = None

    ruleset_id: Optional[str] = None


class Metadata(BaseModel):
    model: str

    processing_time_ms: float

    project: MetadataProject

    provider: str

    requester_id: str

    analyzed_at: Optional[datetime] = None

    event_id: Optional[str] = None


class ModifiedDataInputMessage(BaseModel):
    content: str

    role: Optional[str] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModifiedDataInput(BaseModel):
    messages: Optional[List[ModifiedDataInputMessage]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModifiedDataOutputMessage(BaseModel):
    content: str

    role: Optional[str] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModifiedDataOutput(BaseModel):
    messages: Optional[List[ModifiedDataOutputMessage]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModifiedData(BaseModel):
    input: ModifiedDataInput

    output: ModifiedDataOutput


class InteractionAnalyzeResponse(BaseModel):
    analysis: List[Analysis]

    analyzed_data: AnalyzedData

    metadata: Metadata

    modified_data: ModifiedData
