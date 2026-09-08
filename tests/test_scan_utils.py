# Tests for scan report reconstruction from the summary and paginated file-results endpoints

from __future__ import annotations

from unittest.mock import Mock, call, patch

from hiddenlayer.lib.scan_utils import (
    FILE_RESULTS_PAGE_SIZE,
    FILE_RESULTS_PAGE_DELAY_SECONDS,
    _build_scan_report,
    _collect_file_results,
)


def _mock_file_result(file_id: str) -> Mock:
    file_result = Mock()
    file_result.model_dump.return_value = {"file_instance_id": file_id, "file_location": f"{file_id}.pkl"}
    return file_result


class TestCollectFileResults:
    """Test paginated file-result collection."""

    def test_single_page(self) -> None:
        client = Mock()
        page = Mock()
        page.items = [_mock_file_result("file-1")]
        page.has_next_page.return_value = False
        client.scans.results.list_files.return_value = page

        with patch("hiddenlayer.lib.scan_utils.time.sleep") as mock_sleep:
            results = _collect_file_results(client, scan_id="scan-1")

        assert len(results) == 1
        client.scans.results.list_files.assert_called_once_with("scan-1", page_size=FILE_RESULTS_PAGE_SIZE)
        mock_sleep.assert_not_called()

    def test_multiple_pages_are_throttled(self) -> None:
        client = Mock()
        page3 = Mock()
        page3.items = [_mock_file_result("file-3")]
        page3.has_next_page.return_value = False
        page2 = Mock()
        page2.items = [_mock_file_result("file-2")]
        page2.has_next_page.return_value = True
        page2.get_next_page.return_value = page3
        page1 = Mock()
        page1.items = [_mock_file_result("file-1")]
        page1.has_next_page.return_value = True
        page1.get_next_page.return_value = page2
        client.scans.results.list_files.return_value = page1

        with patch("hiddenlayer.lib.scan_utils.time.sleep") as mock_sleep:
            results = _collect_file_results(client, scan_id="scan-1")

        # Every file from every page, exactly once, in page order
        assert [r.model_dump()["file_instance_id"] for r in results] == ["file-1", "file-2", "file-3"]

        # One throttle sleep before each subsequent page fetch
        assert mock_sleep.call_args_list == [
            call(FILE_RESULTS_PAGE_DELAY_SECONDS),
            call(FILE_RESULTS_PAGE_DELAY_SECONDS),
        ]

    def test_empty_page(self) -> None:
        client = Mock()
        page = Mock()
        page.items = []
        page.has_next_page.return_value = False
        client.scans.results.list_files.return_value = page

        assert _collect_file_results(client, scan_id="scan-1") == []


class TestBuildScanReport:
    """Test assembling a full ScanReport from a summary plus file results."""

    def test_maps_summary_files_and_deprecated_fields(self) -> None:
        summary = Mock()
        summary.model_dump.return_value = {
            "scan_id": "scan-1",
            "status": "done",
            "start_time": "2026-01-01T00:00:00Z",
            "version": "1.0.0",
            "inventory": {"model_name": "test-model", "requested_scan_location": "model.pkl"},
            "summary": {
                "detection_count": 3,
                "file_count": 5,
                "files_with_detections_count": 2,
                "detection_categories": ["malware"],
            },
        }
        file_results = [_mock_file_result("file-1"), _mock_file_result("file-2")]

        report = _build_scan_report(summary, file_results)

        assert report.scan_id == "scan-1"
        assert report.status == "done"
        assert report.file_results is not None and len(report.file_results) == 2

        # Deprecated top-level fields are mirrored from the nested summary
        assert report.detection_count == 3
        assert report.file_count == 5
        assert report.files_with_detections_count == 2
        assert report.detection_categories == ["malware"]

    def test_existing_top_level_fields_are_not_overwritten(self) -> None:
        summary = Mock()
        summary.model_dump.return_value = {
            "scan_id": "scan-1",
            "status": "done",
            "detection_count": 7,
            "summary": {"detection_count": 3, "file_count": 1, "files_with_detections_count": 1},
        }

        report = _build_scan_report(summary, [])

        assert report.detection_count == 7
