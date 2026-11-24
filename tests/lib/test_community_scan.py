from __future__ import annotations

import httpx
import pytest
from fake_scan_api import API_URL, SCAN_ID, FakeScanApi

from hiddenlayer import AsyncHiddenLayer, HiddenLayer
from hiddenlayer.lib import CommunityScanSource, scan_utils

JOBS_PATH = "/scan/v3/jobs"
PRESIGNED_MODEL_URL = "https://acme-models.s3.amazonaws.com/release/model.pkl?X-Amz-Signature=3f9c"


def sync_client(api: FakeScanApi) -> HiddenLayer:
    return HiddenLayer(
        token="test-token", base_url=API_URL, httpx_client=httpx.Client(transport=api.transport), max_retries=0
    )


def async_client(api: FakeScanApi) -> AsyncHiddenLayer:
    return AsyncHiddenLayer(
        token="test-token", base_url=API_URL, httpx_client=httpx.AsyncClient(transport=api.transport), max_retries=0
    )


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    async def skip(delay: float) -> None:
        return None

    monkeypatch.setattr(scan_utils.time, "sleep", lambda delay: None)
    monkeypatch.setattr(scan_utils.asyncio, "sleep", skip)


def test_community_scan_requests_the_scan_and_waits_for_its_report() -> None:
    api = FakeScanApi(summaries=["pending", "running", "done"])

    report = sync_client(api).community_scanner.community_scan(
        model_name="sentiment-classifier",
        model_path=PRESIGNED_MODEL_URL,
        model_source=CommunityScanSource.AWS_PRESIGNED,
    )

    assert api.body("POST", JOBS_PATH) == {
        "access": {"source": "AWS_PRESIGNED"},
        "inventory": {
            "model_name": "sentiment-classifier",
            "model_version": "main",
            "requested_scan_location": PRESIGNED_MODEL_URL,
            "requesting_entity": "hiddenlayer-python-sdk",
            "request_source": "API Upload",
            "origin": "",
        },
    }
    assert report.scan_id == SCAN_ID
    assert report.status == "done"


def test_community_scan_without_waiting_returns_the_report_as_it_stands() -> None:
    api = FakeScanApi(summaries=["running"])

    report = sync_client(api).community_scanner.community_scan(
        "sentiment-classifier", "acme/sentiment-classifier", "HUGGING_FACE", wait_for_results=False
    )

    assert report.status == "running"
    assert len(api.calls("GET", f"/scan/v3/results/{SCAN_ID}/summary")) == 1


def test_community_scan_passes_the_version_request_source_and_origin() -> None:
    api = FakeScanApi()

    sync_client(api).community_scanner.community_scan(
        model_name="sentiment-classifier",
        model_path="acme/sentiment-classifier",
        model_source="HUGGING_FACE",
        model_version="v2.1",
        request_source="Integration",
        origin="Hugging Face",
    )

    inventory = api.body("POST", JOBS_PATH)["inventory"]
    assert (inventory["model_version"], inventory["request_source"], inventory["origin"]) == (
        "v2.1",
        "Integration",
        "Hugging Face",
    )


def test_community_scan_fails_when_the_api_returns_no_scan_id() -> None:
    api = FakeScanApi()
    del api.scan_job_response["scan_id"]

    with pytest.raises(ValueError, match="scan_id must have a value"):
        sync_client(api).community_scanner.community_scan(
            "sentiment-classifier", PRESIGNED_MODEL_URL, CommunityScanSource.AWS_PRESIGNED
        )


def test_scan_result_returns_the_report_of_an_earlier_scan() -> None:
    report = sync_client(FakeScanApi(summaries=["canceled"])).community_scanner.scan_result(scan_id=SCAN_ID)

    assert report.status == "canceled"


async def test_async_community_scan_requests_the_scan_and_waits_for_its_report() -> None:
    api = FakeScanApi(summaries=["running", "done"])

    report = await async_client(api).community_scanner.community_scan(
        model_name="sentiment-classifier",
        model_path=PRESIGNED_MODEL_URL,
        model_source=CommunityScanSource.AWS_PRESIGNED,
        model_version="v2.1",
    )

    body = api.body("POST", JOBS_PATH)
    assert body["access"] == {"source": "AWS_PRESIGNED"}
    assert body["inventory"]["model_version"] == "v2.1"
    assert report.status == "done"


async def test_async_community_scan_without_waiting_returns_the_report_as_it_stands() -> None:
    api = FakeScanApi(summaries=["pending"])

    report = await async_client(api).community_scanner.community_scan(
        "sentiment-classifier", "acme/sentiment-classifier", "HUGGING_FACE", wait_for_results=False
    )

    assert report.status == "pending"


async def test_async_community_scan_fails_when_the_api_returns_no_scan_id() -> None:
    api = FakeScanApi()
    del api.scan_job_response["scan_id"]

    with pytest.raises(ValueError, match="scan_id must have a value"):
        await async_client(api).community_scanner.community_scan(
            "sentiment-classifier", PRESIGNED_MODEL_URL, CommunityScanSource.AWS_PRESIGNED
        )
