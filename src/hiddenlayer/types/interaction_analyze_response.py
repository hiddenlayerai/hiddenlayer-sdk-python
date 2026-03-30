# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

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
    "Evaluation",
]


class AnalysisFindingsFramework(BaseModel):
    label: str
    """Unique identifier for the framework taxonomy item."""

    name: str
    """Name of the framework taxonomy item."""


class AnalysisFindings(BaseModel):
    """The frameworks and associated findings for the analysis."""

    frameworks: Dict[str, List[AnalysisFindingsFramework]]
    """The taxonomies for the detections."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Analysis(BaseModel):
    id: str
    """The unique identifier for the analyzer."""

    configuration: Dict[str, object]
    """The configuration settings used for the analyzer."""

    detected: bool
    """Indicates the analysis resulted in a detection."""

    findings: AnalysisFindings
    """The frameworks and associated findings for the analysis."""

    name: str
    """The name of the analysis performed."""

    phase: str
    """The phase of the analysis (i.e. input or output)."""

    processing_time_ms: float
    """The time taken to perform this specific analysis."""

    version: str
    """The version of the analysis performed."""


class AnalyzedDataInputMessage(BaseModel):
    content: str
    """The textual content of the message."""

    role: Optional[str] = None
    """The role of the message sender (e.g., user, assistant, system)."""


class AnalyzedDataInput(BaseModel):
    messages: Optional[List[AnalyzedDataInputMessage]] = None
    """The list of messages as input to a language model."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class AnalyzedDataOutputMessage(BaseModel):
    content: str
    """The textual content of the message."""

    role: Optional[str] = None
    """The role of the message sender (e.g., user, assistant, system)."""


class AnalyzedDataOutput(BaseModel):
    messages: Optional[List[AnalyzedDataOutputMessage]] = None
    """The list of messages as output from a language model."""


class AnalyzedData(BaseModel):
    """The language model input and/or output that was analyzed."""

    input: AnalyzedDataInput

    output: Optional[AnalyzedDataOutput] = None


class MetadataProject(BaseModel):
    project_alias: Optional[str] = None
    """A custom alias for the Project."""

    project_id: Optional[str] = None
    """The unique identifier for the Project."""

    ruleset_id: Optional[str] = None
    """The unique identifier for the Ruleset associated with the Project."""


class Metadata(BaseModel):
    model: str
    """The language model from the request."""

    processing_time_ms: float
    """The total time taken to perform the analysis."""

    project: MetadataProject

    provider: str
    """The provider of the language model from the request."""

    requester_id: str
    """The identifier for the entity from the request."""

    analyzed_at: Optional[datetime] = None
    """The timestamp when the analysis was performed."""

    event_id: Optional[str] = None
    """The unique identifier for the analysis event."""


class ModifiedDataInputMessage(BaseModel):
    content: str
    """The textual content of the message."""

    role: Optional[str] = None
    """The role of the message sender (e.g., user, assistant, system)."""


class ModifiedDataInput(BaseModel):
    messages: Optional[List[ModifiedDataInputMessage]] = None
    """The list of messages as input to a language model."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ModifiedDataOutputMessage(BaseModel):
    content: str
    """The textual content of the message."""

    role: Optional[str] = None
    """The role of the message sender (e.g., user, assistant, system)."""


class ModifiedDataOutput(BaseModel):
    messages: Optional[List[ModifiedDataOutputMessage]] = None
    """The list of messages as output from a language model."""


class ModifiedData(BaseModel):
    """
    The potentially modified language model input and output after applying any redactions or modifications based on the analysis.
    """

    input: ModifiedDataInput

    output: ModifiedDataOutput


class Evaluation(BaseModel):
    """The evaluation of the analysis results."""

    action: Literal["Allow", "Alert", "Redact", "Block"]
    """The action based on interaction analysis and configured tenant security rules."""

    has_detections: bool
    """Indicates if any detections were found during the analysis."""

    threat_level: Literal["None", "Low", "Medium", "High", "Critical"]
    """
    The threat level based on interaction analysis and configured tenant security
    rules.
    """


class InteractionAnalyzeResponse(BaseModel):
    analysis: List[Analysis]

    analyzed_data: AnalyzedData
    """The language model input and/or output that was analyzed."""

    metadata: Metadata

    modified_data: ModifiedData
    """
    The potentially modified language model input and output after applying any
    redactions or modifications based on the analysis.
    """

    evaluation: Optional[Evaluation] = None
    """The evaluation of the analysis results."""
