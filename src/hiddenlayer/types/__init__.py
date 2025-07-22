# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .shared import (
    Node as Node,
    Region as Region,
    Message as Message,
    Exception as Exception,
    PropertyBag as PropertyBag,
    ArtifactContent as ArtifactContent,
    MultiformatMessageString as MultiformatMessageString,
)
from .model_create_params import ModelCreateParams as ModelCreateParams
from .sensor_query_params import SensorQueryParams as SensorQueryParams
from .sensor_create_params import SensorCreateParams as SensorCreateParams
from .sensor_update_params import SensorUpdateParams as SensorUpdateParams
from .model_create_response import ModelCreateResponse as ModelCreateResponse
from .sensor_query_response import SensorQueryResponse as SensorQueryResponse
from .sensor_create_response import SensorCreateResponse as SensorCreateResponse
from .sensor_update_response import SensorUpdateResponse as SensorUpdateResponse
from .model_retrieve_response import ModelRetrieveResponse as ModelRetrieveResponse
from .sensor_retrieve_response import SensorRetrieveResponse as SensorRetrieveResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    shared.exception.Exception.model_rebuild(_parent_namespace_depth=0)
    shared.node.Node.model_rebuild(_parent_namespace_depth=0)
else:
    shared.exception.Exception.update_forward_refs()  # type: ignore
    shared.node.Node.update_forward_refs()  # type: ignore
