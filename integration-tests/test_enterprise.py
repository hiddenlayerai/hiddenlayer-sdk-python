import pickle

import pytest

from hiddenlayer import HiddenlayerServiceClient


class MaliciousPickle:
    def __reduce__(self):
        return exec, ("import os; os.system('env')",)


@pytest.mark.xfail
def test_scan_model_enterprise(tmp_path):
    hl_client = HiddenlayerServiceClient(host="http://localhost:8000")

    model_path = tmp_path / "model.pkl"
    malicious_model = MaliciousPickle()

    with open(model_path, "wb") as f:
        pickle.dump(malicious_model, f)

    results = hl_client.model_scanner.scan_file(
        model_name="sdk-integration-scan_model", model_path=model_path
    )

    detections = results.detections

    assert detections
    assert detections[0]["severity"] == "MALICIOUS"
    assert "system" in detections[0]["description"]
