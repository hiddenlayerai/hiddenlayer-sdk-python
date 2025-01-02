import os
import pickle
import sys
from typing import Optional
from uuid import uuid4

import pytest

from hiddenlayer import HiddenlayerServiceClient
from hiddenlayer.sdk.models import ScanResults

params = [
    ("https://api.us.hiddenlayer.ai"),
    pytest.param("http://localhost:8000", marks=pytest.mark.xfail),
]

sys.path = [os.path.join(os.pardir, 'hiddenlayer', 'sdk')] + sys.path


class MaliciousPickle:
    def __reduce__(self):
        return exec, ("import os; os.system('env')",)


class SafePickle:
    def __reduce__(self):
        return print, ("Hello, World!",)


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

    model_path = _setup_scan_model(tmp_path)
    model_name = f"sdk-integration-scan-model-{uuid4()}"

    results = hl_client.model_scanner.scan_file(
        model_name=model_name, model_path=model_path
    )

    _validate_scan_model(results)

    if hl_client.is_saas:
        hl_client.model.delete(model_name=model_name)


def test_scan_folder(tmp_path, hl_client: HiddenlayerServiceClient):
    """Integration test to scan a folder"""

    _setup_scan_folder(tmp_path)
    model_name = f"sdk-integration-scan-model-folder-{uuid4()}"

    results = hl_client.model_scanner.scan_folder(model_name=model_name, path=tmp_path)

    _validate_scan_folder(tmp_path, results)


def test_scan_model_with_version(tmp_path, hl_client: HiddenlayerServiceClient):
    """Integration test to scan a model with a specified version"""

    model_path = _setup_scan_model(tmp_path)
    model_name = f"sdk-integration-scan-model-{uuid4()}"
    model_version = 123

    results = hl_client.model_scanner.scan_file(
        model_name=model_name, model_version=model_version, model_path=model_path
    )

    _validate_scan_model(results)

    assert results.inventory.model_version == str(model_version)

    if hl_client.is_saas:
        hl_client.model.delete(model_name=model_name)


def test_scan_folder_with_version(tmp_path, hl_client: HiddenlayerServiceClient):
    """Integration test to scan a folder with a specified version"""

    _setup_scan_folder(tmp_path)
    model_name = f"sdk-integration-scan-model-folder-{uuid4()}"
    model_version = 123

    results = hl_client.model_scanner.scan_folder(
        model_name=model_name, model_version=model_version, path=tmp_path
    )

    _validate_scan_folder(tmp_path, results)

    assert results.inventory.model_version == str(model_version)


def test_scan_model_multiple_times(tmp_path, hl_client: HiddenlayerServiceClient):
    """Integration test to scan a model multiple times"""

    model_path = _setup_scan_model(tmp_path)
    model_name = f"sdk-integration-scan-model-{uuid4()}"

    results: Optional[ScanResults] = None
    for _ in range(3):
        results = hl_client.model_scanner.scan_file(
            model_name=model_name, model_path=model_path
        )

    assert results is not None

    _validate_scan_model(results)
    assert results.inventory.model_version == "3"

    if hl_client.is_saas:
        hl_client.model.delete(model_name=model_name)


def test_get_sarif_results(tmp_path, hl_client: HiddenlayerServiceClient):
    """Integration test to get sarif results"""

    model_path = _setup_scan_model(tmp_path)
    model_name = f"sdk-integration-scan-model-{uuid4()}"

    results = hl_client.model_scanner.scan_file(
        model_name=model_name, model_path=model_path
    )

    _validate_scan_model(results)

    sarif_results = hl_client.model_scanner.get_sarif_results(model_name=model_name)
    print(sarif_results)

    assert sarif_results is not None
    assert sarif_results.version == "2.1.0"
    assert sarif_results.runs is not None
    run = sarif_results.runs[0]
    assert run.tool.driver.name == "HiddenLayer Model Scanner"
    assert run.results is not None
    results = run.results[0]
    assert results.level == "error"
    assert results.rule_id == "PICKLE_0017_202408"

    if hl_client.is_saas:
        hl_client.model.delete(model_name=model_name)


def _setup_scan_model(tmp_path):
    model_path = tmp_path / "model.pkl"
    malicious_model = MaliciousPickle()

    with open(model_path, "wb") as f:
        pickle.dump(malicious_model, f)

    return model_path


def _validate_scan_model(results: ScanResults):
    assert results.file_count == 1
    assert results.files_with_detections_count == 1

    assert results.file_results is not None
    file_results = results.file_results[0]

    detections = file_results.detections

    assert file_results.details.file_type_details is not None
    assert file_results.details.file_type_details["pickle_modules"] == [
        "callable: builtins.exec"
    ]

    assert detections
    assert detections[0].severity == "high"
    assert (
        "This detection rule was triggered by the presence of a function or library that can be used to execute code"
        in str(detections[0].description)
    )


def _setup_scan_folder(tmp_path):
    safe_model_path = tmp_path / "safe_model.pkl"
    malicious_model_path = tmp_path / "malicious_model.pkl"
    model_name = f"sdk-integration-scan-model-folder-{uuid4()}"

    with open(safe_model_path, "wb") as f:
        pickle.dump(SafePickle(), f)

    with open(malicious_model_path, "wb") as f:
        pickle.dump(MaliciousPickle(), f)


def _validate_scan_folder(tmp_path, results: ScanResults):
    safe_model = "safe_model.pkl"
    malicious_model = "malicious_model.pkl"

    assert results.file_count == 3
    assert results.files_with_detections_count == 2

    assert results.file_results is not None
    safe_model_found = False
    malicious_model_found = False
    for top_file_results in results.file_results:
        for file_results in top_file_results.file_results:
            if file_results.file_location.endswith(safe_model):
                detections = file_results.detections
                assert detections is None
                assert file_results.details.file_type_details is not None
                assert file_results.details.file_type_details["pickle_modules"] == [
                    "callable: builtins.print"
                ]
                safe_model_found = True
            elif file_results.file_location.endswith(malicious_model):
                detections = file_results.detections
                assert file_results.details.file_type_details is not None
                assert file_results.details.file_type_details["pickle_modules"] == [
                    "callable: builtins.exec"
                ]
                assert detections
                assert detections[0].severity == "high"
                assert (
                    "This detection rule was triggered by the presence of a function or library that can be used to execute code"
                    in str(detections[0].description)
                )
                assert file_results.details.file_type_details["pickle_modules"] == [
                    "callable: builtins.exec"
                ]
                malicious_model_found = True
    assert safe_model_found
    assert malicious_model_found
