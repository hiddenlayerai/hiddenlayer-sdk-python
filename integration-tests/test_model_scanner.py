import os
import pickle
from uuid import uuid4

import pytest

from hiddenlayer import HiddenlayerServiceClient

params = [
    ("https://api.us.hiddenlayer.ai"),
    pytest.param("http://localhost:8000", marks=pytest.mark.xfail),
]


class MaliciousPickle:
    def __reduce__(self):
        return exec, ("import os; os.system('env')",)


@pytest.fixture(params=params)
def hl_client(request) -> HiddenlayerServiceClient:
    hl_client_id = os.getenv("HL_CLIENT_ID")
    hl_client_secret = os.getenv("HL_CLIENT_SECRET")

    if not hl_client_id:
        raise RuntimeError("HL_CLIENT_ID env var not set.")

    if not hl_client_secret:
        raise RuntimeError("HL_CLIENT_SECRET env var not set.")

    return HiddenlayerServiceClient(
        api_id=hl_client_id, api_key=hl_client_secret, host=request.param
    )


def test_scan_model(tmp_path, hl_client: HiddenlayerServiceClient):
    """Integration test to scan a model"""

    model_path = tmp_path / "model.pkl"
    malicious_model = MaliciousPickle()
    model_name = f"sdk-integration-scan-model-{uuid4()}"

    with open(model_path, "wb") as f:
        pickle.dump(malicious_model, f)

    results = hl_client.model_scanner.scan_file(
        model_name=model_name, model_path=model_path
    )

    detections = results.detections

    assert results.results.pickle_modules == ["builtins.exec"]

    assert detections
    assert detections[0]["severity"] == "MALICIOUS"
    assert "system" in detections[0]["description"]

    if hl_client.is_saas:
        hl_client.model.delete(model_name=model_name)
