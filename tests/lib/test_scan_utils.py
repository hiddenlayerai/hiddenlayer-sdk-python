from __future__ import annotations

from typing import List

import httpx
import pytest
from fake_scan_api import API_URL, NOT_FOUND, SCAN_ID, TIMED_OUT, FakeScanApi

from hiddenlayer import AsyncHiddenLayer, HiddenLayer
from hiddenlayer.errors import NotFoundError
from hiddenlayer.lib import scan_utils
from hiddenlayer.lib.scan_utils import (
    get_scan_results,
    get_scan_results_async,
    wait_for_scan_results,
    wait_for_scan_results_async,
)
from hiddenlayer.types import ScanReportSummaryV3Summary

SUMMARY_PATH = f"/scan/v3/results/{SCAN_ID}/summary"
FILES_PATH = f"/scan/v3/results/{SCAN_ID}/files"


def sync_client(api: FakeScanApi) -> HiddenLayer:
    return HiddenLayer(
        token="test-token", base_url=API_URL, httpx_client=httpx.Client(transport=api.transport), max_retries=0
    )


def async_client(api: FakeScanApi) -> AsyncHiddenLayer:
    return AsyncHiddenLayer(
        token="test-token", base_url=API_URL, httpx_client=httpx.AsyncClient(transport=api.transport), max_retries=0
    )


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> List[float]:
    """The delays the helpers asked for, in order, with the jitter taken out and nothing actually slept."""
    delays: List[float] = []

    async def record(delay: float) -> None:
        delays.append(delay)

    monkeypatch.setattr(scan_utils.time, "sleep", delays.append)
    monkeypatch.setattr(scan_utils.asyncio, "sleep", record)
    monkeypatch.setattr(scan_utils.random, "uniform", lambda low, high: 0.0)
    return delays


def test_get_scan_results_reads_every_page_with_a_pause_between_pages(sleeps: List[float]) -> None:
    names = [f"weights-{number:03}.bin" for number in range(250)]
    api = FakeScanApi(files=names)

    report = get_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert [result.file_location for result in report.file_results or []] == names
    assert [request.url.params["page_size"] for request in api.calls("GET", FILES_PATH)] == ["100", "100", "100"]
    assert sleeps == [0.25, 0.25]


def test_report_mirrors_the_deprecated_top_level_fields_from_the_summary(sleeps: List[float]) -> None:
    report = get_scan_results(sync_client(FakeScanApi(files=["model.pkl", "config.json"])), scan_id=SCAN_ID)

    assert report.detection_count == 3
    assert report.file_count == 2
    assert report.files_with_detections_count == 2
    assert report.detection_categories == ["Arbitrary Code Execution"]
    assert report.severity == "high"


def test_report_keeps_a_top_level_field_the_api_returns(sleeps: List[float]) -> None:
    api = FakeScanApi(summary_fields={"detection_count": 7})

    report = get_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert report.detection_count == 7


def test_report_keeps_aliased_fields_and_nested_models(sleeps: List[float]) -> None:
    report = get_scan_results(sync_client(FakeScanApi()), scan_id=SCAN_ID)

    assert report.scan_id == SCAN_ID
    assert report.schema_version == "3.2.0"
    assert report.inventory.model_name == "sentiment-classifier"
    assert isinstance(report.summary, ScanReportSummaryV3Summary)
    assert report.file_results is not None
    assert report.file_results[0].details.file_type == "pickle"


def test_get_scan_results_retries_a_scan_that_is_not_found_yet(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[NOT_FOUND, NOT_FOUND, "running"])

    report = get_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert report.status == "running"
    assert sleeps == [0.5, 1.0]


def test_get_scan_results_gives_up_after_five_attempts(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[NOT_FOUND])

    with pytest.raises(NotFoundError):
        get_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert len(api.calls("GET", SUMMARY_PATH)) == 5
    assert sleeps == [0.5, 1.0, 1.5, 2.0]


@pytest.mark.parametrize("final_status", ["done", "failed", "canceled"])
def test_wait_for_scan_results_polls_until_the_scan_ends(final_status: str, sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[NOT_FOUND, "pending", "running", final_status])

    report = wait_for_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert report.status == final_status
    assert sleeps == [0.2, 0.4, 0.8]


def test_wait_for_scan_results_backs_off_to_30_seconds_at_most(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=["running"] * 12 + ["done"])

    wait_for_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert sleeps[:3] == [0.2, 0.4, 0.8]
    assert max(sleeps) == 30
    assert sleeps[-1] == 30


def test_wait_for_scan_results_keeps_polling_a_scan_that_runs_for_hours(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=["running"] * 1100 + ["done"])

    report = wait_for_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert report.status == "done"
    assert sleeps[-1] == 30


def test_wait_for_scan_results_polls_through_requests_that_time_out(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=["running", TIMED_OUT, TIMED_OUT, "running", TIMED_OUT, TIMED_OUT, "done"])

    report = wait_for_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert report.status == "done"
    assert len(api.calls("GET", SUMMARY_PATH)) == 7


def test_wait_for_scan_results_gives_up_after_three_timeouts_in_a_row(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=["running", TIMED_OUT])

    with pytest.raises(httpx.ReadTimeout):
        wait_for_scan_results(sync_client(api), scan_id=SCAN_ID)

    assert len(api.calls("GET", SUMMARY_PATH)) == 4


async def test_async_wait_for_scan_results_polls_through_requests_that_time_out(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[TIMED_OUT, TIMED_OUT, "done"])

    report = await wait_for_scan_results_async(async_client(api), scan_id=SCAN_ID)

    assert report.status == "done"


async def test_async_wait_for_scan_results_gives_up_after_three_timeouts_in_a_row(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[TIMED_OUT])

    with pytest.raises(httpx.ReadTimeout):
        await wait_for_scan_results_async(async_client(api), scan_id=SCAN_ID)

    assert len(api.calls("GET", SUMMARY_PATH)) == 3


async def test_async_get_scan_results_reads_every_page_and_retries_not_found(sleeps: List[float]) -> None:
    names = [f"weights-{number:03}.bin" for number in range(150)]
    api = FakeScanApi(summaries=[NOT_FOUND, "done"], files=names)

    report = await get_scan_results_async(async_client(api), scan_id=SCAN_ID)

    assert [result.file_location for result in report.file_results or []] == names
    assert report.detection_count == 3
    assert sleeps == [0.5, 0.25]


async def test_async_get_scan_results_gives_up_after_five_attempts(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[NOT_FOUND])

    with pytest.raises(NotFoundError):
        await get_scan_results_async(async_client(api), scan_id=SCAN_ID)

    assert len(api.calls("GET", SUMMARY_PATH)) == 5


async def test_async_wait_for_scan_results_polls_until_the_scan_ends(sleeps: List[float]) -> None:
    api = FakeScanApi(summaries=[NOT_FOUND, "running", "done"])

    report = await wait_for_scan_results_async(async_client(api), scan_id=SCAN_ID)

    assert report.status == "done"
    assert sleeps == [0.2, 0.4]
