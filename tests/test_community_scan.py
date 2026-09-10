# Tests for custom community scan functionality

from __future__ import annotations

from unittest.mock import Mock, AsyncMock, patch

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from hiddenlayer.types.scans import ScanJob
from hiddenlayer.lib.scan_utils import ScanStatus
from hiddenlayer.lib.community_scan import CommunityScanner, CommunityScanSource, AsyncCommunityScanner


def _mock_report_reconstruction(mock_client: Mock, *, status: str = "done") -> None:
    """Configure retrieve_summary + list_files so helpers can assemble a report."""
    summary = Mock()
    summary.status = status
    summary.model_dump.return_value = {
        "scan_id": "test-scan-id-123",
        "status": status,
        "summary": {"detection_count": 0, "file_count": 1, "files_with_detections_count": 0},
    }
    file_result = Mock()
    file_result.model_dump.return_value = {"file_instance_id": "file-1", "file_location": "model.pkl"}
    page = Mock()
    page.items = [file_result]
    page.has_next_page.return_value = False
    mock_client.scans.results.retrieve_summary.return_value = summary
    mock_client.scans.results.list_files.return_value = page


class TestCommunityScannerIntegration:
    """Test that community scanner is properly integrated into the main clients."""

    def test_sync_client_has_community_scanner(self) -> None:
        """Test that HiddenLayer client has community_scanner property."""
        client = HiddenLayer(bearer_token="test-token")

        assert hasattr(client, "community_scanner")
        assert isinstance(client.community_scanner, CommunityScanner)

    def test_async_client_has_community_scanner(self) -> None:
        """Test that AsyncHiddenLayer client has community_scanner property."""
        client = AsyncHiddenLayer(bearer_token="test-token")

        assert hasattr(client, "community_scanner")
        assert isinstance(client.community_scanner, AsyncCommunityScanner)


class TestCommunityScanner:
    """Test the CommunityScanner class functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_client = Mock()
        self.scanner = CommunityScanner(self.mock_client)

    def test_init(self) -> None:
        """Test CommunityScanner initialization."""
        assert self.scanner._client is self.mock_client

    def test_community_scan_without_waiting(self) -> None:
        """Test community_scan with wait_for_results=False."""
        # Mock the scan job response
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = "test-scan-id-123"

        # Mock the jobs.request method
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        # Mock the summary + file results used to assemble the report
        _mock_report_reconstruction(self.mock_client, status="pending")

        # Call community_scan without waiting
        result = self.scanner.community_scan(
            model_name="test-model",
            model_path="https://example.com/model.pkl",
            model_source="AWS_PRESIGNED",
            wait_for_results=False,
        )

        # Verify the request was made correctly
        self.mock_client.scans.jobs.request.assert_called_once()
        call_args = self.mock_client.scans.jobs.request.call_args

        assert call_args[1]["access"]["source"] == "AWS_PRESIGNED"
        assert call_args[1]["inventory"]["model_name"] == "test-model"
        assert call_args[1]["inventory"]["requested_scan_location"] == "https://example.com/model.pkl"
        assert call_args[1]["inventory"]["requesting_entity"] == "hiddenlayer-python-sdk"

        # Should fetch the summary once and never touch the legacy results endpoint
        self.mock_client.scans.results.retrieve_summary.assert_called_once_with("test-scan-id-123")
        self.mock_client.scans.jobs.retrieve.assert_not_called()
        assert result.scan_id == "test-scan-id-123"
        assert result.status == "pending"
        assert result.file_results is not None and len(result.file_results) == 1

    @patch("hiddenlayer.lib.scan_utils.time.sleep")
    @patch("hiddenlayer.lib.scan_utils.logger")
    def test_community_scan_with_waiting_success(self, mock_logger: Mock, mock_sleep: Mock) -> None:
        """Test community_scan with wait_for_results=True until success."""
        # Mock the scan job response
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = "test-scan-id-123"
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        # Mock the polling sequence: pending -> running -> done
        mock_summaries: list[Mock] = []
        for status in ["pending", "running", "done"]:
            mock_summary = Mock()
            mock_summary.scan_id = "test-scan-id-123"
            mock_summary.status = status
            mock_summaries.append(mock_summary)

        mock_summaries[-1].model_dump.return_value = {
            "scan_id": "test-scan-id-123",
            "status": "done",
            "summary": {"detection_count": 1, "file_count": 2, "files_with_detections_count": 1},
        }
        self.mock_client.scans.results.retrieve_summary.side_effect = mock_summaries

        # File results are collected from the paginated endpoint once the scan is done
        mock_file_result = Mock()
        mock_file_result.model_dump.return_value = {"file_instance_id": "file-1", "file_location": "model.pkl"}
        mock_page = Mock()
        mock_page.items = [mock_file_result]
        mock_page.has_next_page.return_value = False
        self.mock_client.scans.results.list_files.return_value = mock_page

        # Call community_scan with waiting
        result = self.scanner.community_scan(
            model_name="test-model",
            model_path="https://example.com/model.pkl",
            model_source="AWS_PRESIGNED",
            wait_for_results=True,
        )

        # Should make the request
        self.mock_client.scans.jobs.request.assert_called_once()

        # Should poll the summary endpoint, then collect file results; the legacy
        # unpaginated results endpoint is never called
        assert self.mock_client.scans.results.retrieve_summary.call_count == 3
        self.mock_client.scans.results.list_files.assert_called_once()
        self.mock_client.scans.jobs.retrieve.assert_not_called()

        # Should have slept between polls
        assert mock_sleep.call_count == 2

        # Should have logged status updates
        assert mock_logger.info.call_count == 2

        # Final result is assembled from the summary plus file results
        assert result.scan_id == "test-scan-id-123"
        assert result.status == "done"
        assert result.file_results is not None and len(result.file_results) == 1
        # Deprecated top-level counts are mirrored from the nested summary
        assert result.detection_count == 1
        assert result.file_count == 2

    def test_community_scan_no_scan_id_raises_error(self) -> None:
        """Test that missing scan_id raises ValueError."""
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = None  # No scan ID
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        with pytest.raises(ValueError, match="scan_id must have a value"):
            self.scanner.community_scan(
                model_name="test-model", model_path="https://example.com/model.pkl", model_source="AWS_PRESIGNED"
            )

    def test_community_scan_with_custom_parameters(self) -> None:
        """Test community_scan with all custom parameters."""
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = "test-scan-id-123"
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        _mock_report_reconstruction(self.mock_client)

        self.scanner.community_scan(
            model_name="custom-model",
            model_path="https://custom.com/model.bin",
            model_source="HUGGING_FACE",
            model_version="v2.0",
            wait_for_results=False,
            request_source="Integration",
            origin="CustomOrigin",
        )

        call_args = self.mock_client.scans.jobs.request.call_args
        inventory = call_args[1]["inventory"]

        assert inventory["model_name"] == "custom-model"
        assert inventory["model_version"] == "v2.0"
        assert inventory["requested_scan_location"] == "https://custom.com/model.bin"
        assert inventory["request_source"] == "Integration"
        assert inventory["origin"] == "CustomOrigin"
        assert call_args[1]["access"]["source"] == "HUGGING_FACE"


class TestAsyncCommunityScanner:
    """Test the AsyncCommunityScanner class functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_client = AsyncMock()
        self.scanner = AsyncCommunityScanner(self.mock_client)

    def test_init(self) -> None:
        """Test AsyncCommunityScanner initialization."""
        assert self.scanner._client is self.mock_client

    @pytest.mark.asyncio
    async def test_async_community_scan_without_waiting(self) -> None:
        """Test async community_scan with wait_for_results=False."""
        # Mock the scan job response
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = "test-scan-id-123"
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        # Mock the summary + file results used to assemble the report
        _mock_report_reconstruction(self.mock_client, status="pending")

        # Call community_scan without waiting
        result = await self.scanner.community_scan(
            model_name="test-model",
            model_path="https://example.com/model.pkl",
            model_source="AWS_PRESIGNED",
            wait_for_results=False,
        )

        # Verify the request was made correctly
        self.mock_client.scans.jobs.request.assert_called_once()
        call_args = self.mock_client.scans.jobs.request.call_args

        assert call_args[1]["access"]["source"] == "AWS_PRESIGNED"
        assert call_args[1]["inventory"]["model_name"] == "test-model"

        # Should fetch the summary once and never touch the legacy results endpoint
        self.mock_client.scans.results.retrieve_summary.assert_called_once_with("test-scan-id-123")
        self.mock_client.scans.jobs.retrieve.assert_not_called()
        assert result.scan_id == "test-scan-id-123"
        assert result.status == "pending"
        assert result.file_results is not None and len(result.file_results) == 1

    @pytest.mark.asyncio
    @patch("hiddenlayer.lib.scan_utils.asyncio.sleep", new_callable=AsyncMock)
    @patch("hiddenlayer.lib.scan_utils.logger")
    async def test_async_community_scan_with_waiting_success(self, mock_logger: Mock, mock_sleep: AsyncMock) -> None:
        """Test async community_scan with wait_for_results=True until success."""
        # Mock the scan job response
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = "test-scan-id-123"
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        # Mock the polling sequence: pending -> running -> done
        mock_summaries: list[Mock] = []
        for status in ["pending", "running", "done"]:
            mock_summary = Mock()
            mock_summary.scan_id = "test-scan-id-123"
            mock_summary.status = status
            mock_summaries.append(mock_summary)

        mock_summaries[-1].model_dump.return_value = {
            "scan_id": "test-scan-id-123",
            "status": "done",
            "summary": {"detection_count": 1, "file_count": 2, "files_with_detections_count": 1},
        }
        self.mock_client.scans.results.retrieve_summary.side_effect = mock_summaries

        # File results are collected from the paginated endpoint once the scan is done
        mock_file_result = Mock()
        mock_file_result.model_dump.return_value = {"file_instance_id": "file-1", "file_location": "model.pkl"}
        mock_page = Mock()
        mock_page.items = [mock_file_result]
        mock_page.has_next_page.return_value = False
        self.mock_client.scans.results.list_files.return_value = mock_page

        # Call community_scan with waiting
        result = await self.scanner.community_scan(
            model_name="test-model",
            model_path="https://example.com/model.pkl",
            model_source="AWS_PRESIGNED",
            wait_for_results=True,
        )

        # Should make the request
        self.mock_client.scans.jobs.request.assert_called_once()

        # Should poll the summary endpoint, then collect file results; the legacy
        # unpaginated results endpoint is never called
        assert self.mock_client.scans.results.retrieve_summary.call_count == 3
        self.mock_client.scans.results.list_files.assert_called_once()
        self.mock_client.scans.jobs.retrieve.assert_not_called()

        # Should have slept between polls
        assert mock_sleep.call_count == 2

        # Should have logged status updates
        assert mock_logger.info.call_count == 2

        # Final result is assembled from the summary plus file results
        assert result.scan_id == "test-scan-id-123"
        assert result.status == "done"
        assert result.file_results is not None and len(result.file_results) == 1
        # Deprecated top-level counts are mirrored from the nested summary
        assert result.detection_count == 1
        assert result.file_count == 2


class TestCommunityScanConstants:
    """Test the constants used by community scan."""

    def test_community_scan_source_constants(self) -> None:
        """Test CommunityScanSource constants."""
        assert CommunityScanSource.LOCAL == "LOCAL"
        assert CommunityScanSource.AWS_PRESIGNED == "AWS_PRESIGNED"
        assert CommunityScanSource.AWS_IAM_ROLE == "AWS_IAM_ROLE"
        assert CommunityScanSource.AZURE_BLOB_SAS == "AZURE_BLOB_SAS"
        assert CommunityScanSource.AZURE_BLOB_AD == "AZURE_BLOB_AD"
        assert CommunityScanSource.GOOGLE_SIGNED == "GOOGLE_SIGNED"
        assert CommunityScanSource.GOOGLE_OAUTH == "GOOGLE_OAUTH"
        assert CommunityScanSource.HUGGING_FACE == "HUGGING_FACE"

    def test_scan_status_constants(self) -> None:
        """Test ScanStatus constants."""
        assert ScanStatus.DONE == "done"
        assert ScanStatus.FAILED == "failed"
        assert ScanStatus.PENDING == "pending"
        assert ScanStatus.RUNNING == "running"
        assert ScanStatus.CANCELED == "canceled"
