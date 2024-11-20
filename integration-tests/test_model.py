import os
from uuid import uuid4

import pytest

from hiddenlayer import HiddenlayerServiceClient
from hiddenlayer.sdk.exceptions import IncompatibleModelError
from hiddenlayer.sdk.rest.models.create_sensor_request import CreateSensorRequest


@pytest.fixture(scope="session")
def hl_client() -> HiddenlayerServiceClient:
    hl_client_id = os.getenv("HL_CLIENT_ID")
    hl_client_secret = os.getenv("HL_CLIENT_SECRET")

    if not hl_client_id:
        raise RuntimeError("HL_CLIENT_ID env var not set.")

    if not hl_client_secret:
        raise RuntimeError("HL_CLIENT_SECRET env var not set.")

    return HiddenlayerServiceClient(api_id=hl_client_id, api_key=hl_client_secret)


def test_model_create_delete(hl_client: HiddenlayerServiceClient):
    """
    Tests that we can create a model, as well as deleting it.
    """

    model_name = f"test_model_create_delete_{str(uuid4())}"

    _ = hl_client.model.create(model_name=model_name, model_version=None)

    hl_client.model.delete(model_name=model_name)


def test_deleting_non_adhoc_model_fails(hl_client: HiddenlayerServiceClient):
    """Test deleting non adhoc models fails gracefully."""

    model_name = "undeletable_model"

    _ = hl_client.model._sensor_api.create_sensor(
        CreateSensorRequest(plaintext_name=model_name, adhoc=False)
    )

    with pytest.raises(IncompatibleModelError):
        hl_client.model.delete(model_name=model_name)
