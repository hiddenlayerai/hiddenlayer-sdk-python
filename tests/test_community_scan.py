# Tests for custom community scan functionality

from __future__ import annotations

from unittest.mock import Mock, AsyncMock, patch

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from hiddenlayer.types.scans import ScanJob, ScanReport
from hiddenlayer.lib.scan_utils import ScanStatus
from hiddenlayer.lib.community_scan import CommunityScanner, CommunityScanSource, AsyncCommunityScanner


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

        # Mock the jobs.retrieve method for immediate return
        mock_scan_report = Mock(spec=ScanReport)
        mock_scan_report.scan_id = "test-scan-id-123"
        mock_scan_report.status = "pending"
        self.mock_client.scans.jobs.retrieve.return_value = mock_scan_report

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

        # Should retrieve once to get current status
        self.mock_client.scans.jobs.retrieve.assert_called_once_with("test-scan-id-123")
        assert result is mock_scan_report

    @patch("hiddenlayer.lib.scan_utils.time.sleep")
    @patch("hiddenlayer.lib.scan_utils.logger")
    def test_community_scan_with_waiting_success(self, mock_logger: Mock, mock_sleep: Mock) -> None:
        """Test community_scan with wait_for_results=True until success."""
        # Mock the scan job response
        mock_scan_job = Mock(spec=ScanJob)
        mock_scan_job.scan_id = "test-scan-id-123"
        self.mock_client.scans.jobs.request.return_value = mock_scan_job

        # Mock the polling sequence: pending -> running -> done
        mock_reports: list[Mock] = []
        for status in ["pending", "running", "done"]:
            mock_report = Mock(spec=ScanReport)
            mock_report.scan_id = "test-scan-id-123"
            mock_report.status = status
            mock_reports.append(mock_report)

        self.mock_client.scans.jobs.retrieve.side_effect = mock_reports

        # Call community_scan with waiting
        result = self.scanner.community_scan(
            model_name="test-model",
            model_path="https://example.com/model.pkl",
            model_source="AWS_PRESIGNED",
            wait_for_results=True,
        )

        # Should make the request
        self.mock_client.scans.jobs.request.assert_called_once()

        # Should retrieve multiple times (polling)
        assert self.mock_client.scans.jobs.retrieve.call_count == 3

        # Should have slept between polls
        assert mock_sleep.call_count == 2

        # Should have logged status updates
        assert mock_logger.info.call_count == 2

        # Final result should be the "done" report
        assert result is mock_reports[2]
        assert result.status == "done"

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

        mock_scan_report = Mock(spec=ScanReport)
        self.mock_client.scans.jobs.retrieve.return_value = mock_scan_report

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

        # Mock the jobs.retrieve method for immediate return
        mock_scan_report = Mock(spec=ScanReport)
        mock_scan_report.scan_id = "test-scan-id-123"
        mock_scan_report.status = "pending"
        self.mock_client.scans.jobs.retrieve.return_value = mock_scan_report

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

        # Should retrieve once to get current status
        self.mock_client.scans.jobs.retrieve.assert_called_once_with("test-scan-id-123")
        assert result is mock_scan_report

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
        mock_reports: list[Mock] = []
        for status in ["pending", "running", "done"]:
            mock_report = Mock(spec=ScanReport)
            mock_report.scan_id = "test-scan-id-123"
            mock_report.status = status
            mock_reports.append(mock_report)

        self.mock_client.scans.jobs.retrieve.side_effect = mock_reports

        # Call community_scan with waiting
        result = await self.scanner.community_scan(
            model_name="test-model",
            model_path="https://example.com/model.pkl",
            model_source="AWS_PRESIGNED",
            wait_for_results=True,
        )

        # Should make the request
        self.mock_client.scans.jobs.request.assert_called_once()

        # Should retrieve multiple times (polling)
        assert self.mock_client.scans.jobs.retrieve.call_count == 3

        # Should have slept between polls
        assert mock_sleep.call_count == 2

        # Should have logged status updates
        assert mock_logger.info.call_count == 2

        # Final result should be the "done" report
        assert result is mock_reports[2]
        assert result.status == "done"


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
