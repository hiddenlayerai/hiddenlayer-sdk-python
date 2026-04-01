"""Registry of beta endpoints.

Maps URL paths to qualified method names for runtime warnings.
Maintained manually; add/remove entries as endpoints enter/exit beta.
"""
from __future__ import annotations

BETA_ENDPOINTS: dict[str, str] = {
    "/detection/v2/request-evaluations": "DetectionResource.request_evaluation",
    "/detection/v2/response-evaluations": "DetectionResource.response_evaluation",
}
