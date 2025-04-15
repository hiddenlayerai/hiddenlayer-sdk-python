# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["VectorSubmitVectorsResponse"]


class VectorSubmitVectorsResponse(BaseModel):
    event_time: str

    group_id: str

    requester_id: str

    sensor_id: str

    tenant_id: str
