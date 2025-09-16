# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .input import Input
from .output import Output
from .._models import BaseModel
from .metadata_project import MetadataProject

__all__ = [
    "InteractionAnalyzeResponse",
    "Analysis",
    "AnalysisFindings",
    "AnalysisFindingsFramework",
    "AnalyzedData",
    "Metadata",
    "ModifiedData",
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


class AnalyzedData(BaseModel):
    input: Input

    output: Optional[Output] = None


class Metadata(BaseModel):
    model: str

    processing_time_ms: float

    project: MetadataProject

    provider: str

    requester_id: str

    analyzed_at: Optional[datetime] = None

    event_id: Optional[str] = None


class ModifiedData(BaseModel):
    input: Input

    output: Output


class InteractionAnalyzeResponse(BaseModel):
    analysis: List[Analysis]

    analyzed_data: AnalyzedData

    metadata: Metadata

    modified_data: ModifiedData
