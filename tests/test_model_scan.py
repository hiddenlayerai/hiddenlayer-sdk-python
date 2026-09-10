from __future__ import annotations

import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from hiddenlayer.types.scans import ScanReport
from hiddenlayer.lib.model_scan import (
    EXCLUDE_FILE_TYPES,
    ModelScanner,
    PathInputType,
    AsyncModelScanner,
    filter_path_objects,
)
from hiddenlayer.lib.scan_utils import ScanStatus
from hiddenlayer.types.scans.upload import FileAddResponse
from hiddenlayer.types.scans.upload_start_response import UploadStartResponse
from hiddenlayer.types.scans.upload_complete_all_response import UploadCompleteAllResponse
from hiddenlayer.types.scans.upload.file_complete_response import FileCompleteResponse


class TestModelScannerIntegration:
    """Test that model scanner is properly integrated into the main clients."""

    def test_sync_client_has_model_scanner(self) -> None:
        """Test that HiddenLayer client has model_scanner property."""
        client = HiddenLayer(bearer_token="test-token")

        assert hasattr(client, "model_scanner")
        assert isinstance(client.model_scanner, ModelScanner)

    def test_async_client_has_model_scanner(self) -> None:
        """Test that AsyncHiddenLayer client has model_scanner property."""
        client = AsyncHiddenLayer(bearer_token="test-token")

        assert hasattr(client, "model_scanner")
        assert isinstance(client.model_scanner, AsyncModelScanner)


class TestModelScanner:
    """Test the ModelScanner class functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_client = Mock()
        self.scanner = ModelScanner(self.mock_client)

    def test_init(self) -> None:
        """Test ModelScanner initialization."""
        assert self.scanner._client is self.mock_client

    def test_scan_file_without_waiting(self) -> None:
        """Test scan_file with wait_for_results=False."""
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".pkl") as temp_file:
            temp_file.write("test model data")
            temp_path = temp_file.name

        try:
            # Mock the upload start response
            mock_upload_response = Mock(spec=UploadStartResponse)
            mock_upload_response.scan_id = "test-scan-id-123"

            # Mock the file add response (multipart upload)
            mock_part = Mock()
            mock_part.start_offset = 0
            mock_part.end_offset = 15  # Length of "test model data"
            mock_part.upload_url = "https://example.com/upload-url"
            mock_part.part_number = 1

            mock_file_add_response = Mock(spec=FileAddResponse)
            mock_file_add_response.parts = [mock_part]
            mock_file_add_response.upload_id = "upload-123"

            # Mock the scan report
            mock_scan_report = Mock(spec=ScanReport)
            mock_scan_report.scan_id = "test-scan-id-123"
            mock_scan_report.status = "pending"

            # Set up mocks
            self.mock_client.scans.upload.start.return_value = mock_upload_response
            self.mock_client.scans.upload.file.add.return_value = mock_file_add_response
            self.mock_client.scans.upload.file.complete.return_value = Mock(spec=FileCompleteResponse)
            self.mock_client.scans.upload.complete_all.return_value = Mock(spec=UploadCompleteAllResponse)
            self.mock_client.scans.jobs.retrieve.return_value = mock_scan_report

            # Mock call to put for upload
            mock_response = Mock(raise_for_status=Mock(return_value=None))
            self.mock_client._client = Mock(put=Mock(return_value=Mock(return_value=mock_response)))

            # Call scan_file without waiting
            result = self.scanner.scan_file(
                model_name="test-model",
                model_path=temp_path,
                model_version="1.0",
                wait_for_results=False,
                request_source="API Upload",
                origin="test",
            )

            # Verify calls
            self.mock_client.scans.upload.start.assert_called_once_with(
                model_name="test-model",
                model_version="1.0",
                requesting_entity="hiddenlayer-python-sdk",
                request_source="API Upload",
                origin="test",
            )

            self.mock_client.scans.upload.file.add.assert_called_once_with(
                scan_id="test-scan-id-123", file_name=temp_path, file_content_length=15
            )

            self.mock_client.scans.upload.file.complete.assert_called_once_with(
                file_id="upload-123", scan_id="test-scan-id-123"
            )

            self.mock_client.scans.upload.complete_all.assert_called_once_with(scan_id="test-scan-id-123")

            # Should retrieve scan once (no waiting)
            self.mock_client.scans.jobs.retrieve.assert_called_once_with("test-scan-id-123")

            # Should return the scan report
            assert result is mock_scan_report

            # Verify httpx.put was called
            self.mock_client._client.put.assert_called_once_with(
                "https://example.com/upload-url",
                content=b"test model data",
                headers={"Content-Type": "application/octet-stream"},
                timeout=self.mock_client.timeout,
            )

        finally:
            # Clean up temp file
            os.unlink(temp_path)

    @patch("hiddenlayer.lib.scan_utils.time.sleep")
    @patch("hiddenlayer.lib.scan_utils.logger")
    def test_scan_file_with_waiting_success(self, mock_logger: Mock, mock_sleep: Mock) -> None:
        """Test scan_file with wait_for_results=True until success."""
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".pkl") as temp_file:
            temp_file.write("test model data")
            temp_path = temp_file.name

        try:
            # Mock the upload start response
            mock_upload_response = Mock(spec=UploadStartResponse)
            mock_upload_response.scan_id = "test-scan-id-123"

            # Mock the file add response (multipart upload)
            mock_part = Mock()
            mock_part.start_offset = 0
            mock_part.end_offset = 15
            mock_part.upload_url = "https://example.com/upload-url"

            mock_file_add_response = Mock(spec=FileAddResponse)
            mock_file_add_response.parts = [mock_part]
            mock_file_add_response.upload_id = "upload-123"

            # Mock scan reports - first pending, then running, then done
            pending_report = Mock(spec=ScanReport)
            pending_report.status = ScanStatus.PENDING

            running_report = Mock(spec=ScanReport)
            running_report.status = ScanStatus.RUNNING

            done_report = Mock(spec=ScanReport)
            done_report.status = ScanStatus.DONE

            # Set up mocks
            self.mock_client.scans.upload.start.return_value = mock_upload_response
            self.mock_client.scans.upload.file.add.return_value = mock_file_add_response
            self.mock_client.scans.upload.file.complete.return_value = Mock(spec=FileCompleteResponse)
            self.mock_client.scans.upload.complete_all.return_value = Mock(spec=UploadCompleteAllResponse)
            self.mock_client.scans.jobs.retrieve.side_effect = [pending_report, running_report, done_report]

            # Mock httpx.put
            with patch("httpx.put") as mock_put:
                mock_response = Mock()
                mock_response.raise_for_status.return_value = None
                mock_put.return_value = mock_response

                # Call scan_file with waiting
                result = self.scanner.scan_file(model_name="test-model", model_path=temp_path, wait_for_results=True)

            # Should retrieve scan multiple times (polling)
            assert self.mock_client.scans.jobs.retrieve.call_count == 3

            # Should return the final scan report
            assert result is done_report

            # Should have slept twice (between the 3 retrievals)
            assert mock_sleep.call_count == 2

            # Should have logged status updates
            mock_logger.info.assert_any_call("scan status: pending")
            mock_logger.info.assert_any_call("scan status: running")

        finally:
            # Clean up temp file
            os.unlink(temp_path)

    def test_scan_folder_functionality(self) -> None:
        """Test scan_folder with file filtering."""
        # Create a temporary directory structure
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create test files
            (temp_path / "model.pkl").write_text("model data")
            (temp_path / "config.json").write_text('{"test": "config"}')
            (temp_path / "README.md").write_text("# Test Model")  # Should be excluded
            (temp_path / "data.txt").write_text("some data")  # Should be excluded
            (temp_path / "subdir").mkdir()
            (temp_path / "subdir" / "weights.pt").write_text("weights")

            # Mock responses
            mock_upload_response = Mock(spec=UploadStartResponse)
            mock_upload_response.scan_id = "test-scan-id-123"

            mock_part = Mock()
            mock_part.start_offset = 0
            mock_part.end_offset = None  # Will read entire file
            mock_part.upload_url = "https://example.com/upload-url"

            mock_file_add_response = Mock(spec=FileAddResponse)
            mock_file_add_response.parts = [mock_part]
            mock_file_add_response.upload_id = "upload-123"

            mock_scan_report = Mock(spec=ScanReport)
            mock_scan_report.status = ScanStatus.DONE

            # Set up mocks
            self.mock_client.scans.upload.start.return_value = mock_upload_response
            self.mock_client.scans.upload.file.add.return_value = mock_file_add_response
            self.mock_client.scans.upload.file.complete.return_value = Mock(spec=FileCompleteResponse)
            self.mock_client.scans.upload.complete_all.return_value = Mock(spec=UploadCompleteAllResponse)
            self.mock_client.scans.jobs.retrieve.return_value = mock_scan_report

            # Mock httpx.put
            with patch("httpx.put") as mock_put:
                mock_response = Mock()
                mock_response.raise_for_status.return_value = None
                mock_put.return_value = mock_response

                # Call scan_folder
                result = self.scanner.scan_folder(model_name="test-model", path=temp_path, wait_for_results=False)

            # Should call file.add for each non-excluded file (model.pkl, config.json, weights.pt)
            # README.md and data.txt should be excluded by EXCLUDE_FILE_TYPES
            assert self.mock_client.scans.upload.file.add.call_count == 3

            # Verify the files that were uploaded
            uploaded_files: list[str] = []
            for call in self.mock_client.scans.upload.file.add.call_args_list:
                uploaded_files.append(Path(call.kwargs["file_name"]).name)

            assert "model.pkl" in uploaded_files
            assert "config.json" in uploaded_files
            assert "weights.pt" in uploaded_files
            assert "README.md" not in uploaded_files  # Should be excluded
            assert "data.txt" not in uploaded_files  # Should be excluded

            assert result is mock_scan_report

    def test_scan_file_upload_url_none_raises_error(self) -> None:
        """Test that None upload_url raises an error."""
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".pkl") as temp_file:
            temp_file.write("test model data")
            temp_path = temp_file.name

        try:
            # Mock responses
            mock_upload_response = Mock(spec=UploadStartResponse)
            mock_upload_response.scan_id = "test-scan-id-123"

            # Mock part with None upload_url
            mock_part = Mock()
            mock_part.start_offset = 0
            mock_part.end_offset = 15
            mock_part.upload_url = None  # This should cause an error

            mock_file_add_response = Mock(spec=FileAddResponse)
            mock_file_add_response.parts = [mock_part]
            mock_file_add_response.upload_id = "upload-123"

            # Set up mocks
            self.mock_client.scans.upload.start.return_value = mock_upload_response
            self.mock_client.scans.upload.file.add.return_value = mock_file_add_response

            # Should raise exception
            with pytest.raises(Exception, match="part.upload_url must not be None"):
                self.scanner.scan_file(model_name="test-model", model_path=temp_path, wait_for_results=False)
        finally:
            # Clean up temp file
            os.unlink(temp_path)


class TestAsyncModelScanner:
    """Test the AsyncModelScanner class functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_client = AsyncMock()
        self.scanner = AsyncModelScanner(self.mock_client)

    def test_init(self) -> None:
        """Test AsyncModelScanner initialization."""
        assert self.scanner._client is self.mock_client

    @pytest.mark.asyncio
    async def test_async_scan_file_without_waiting(self) -> None:
        """Test async scan_file with wait_for_results=False."""
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".pkl") as temp_file:
            temp_file.write("test model data")
            temp_path = temp_file.name

        try:
            # Mock responses
            mock_upload_response = Mock(spec=UploadStartResponse)
            mock_upload_response.scan_id = "test-scan-id-123"

            mock_part = Mock()
            mock_part.start_offset = 0
            mock_part.end_offset = 15
            mock_part.upload_url = "https://example.com/upload-url"

            mock_file_add_response = Mock(spec=FileAddResponse)
            mock_file_add_response.parts = [mock_part]
            mock_file_add_response.upload_id = "upload-123"

            mock_scan_report = Mock(spec=ScanReport)
            mock_scan_report.status = "pending"

            # Set up async mocks - use return_value like other working async tests
            self.mock_client.scans.upload.start.return_value = mock_upload_response
            self.mock_client.scans.upload.file.add.return_value = mock_file_add_response
            self.mock_client.scans.upload.file.complete.return_value = Mock(spec=FileCompleteResponse)
            self.mock_client.scans.upload.complete_all.return_value = Mock(spec=UploadCompleteAllResponse)
            self.mock_client.scans.jobs.retrieve.return_value = mock_scan_report

            # Mock call to put for upload
            mock_response = Mock(raise_for_status=Mock(return_value=None))
            self.mock_client._client = Mock(put=AsyncMock(return_value=Mock(return_value=mock_response)))

            # Call async scan_file
            result = await self.scanner.scan_file(
                model_name="test-model", model_path=temp_path, wait_for_results=False
            )

            # Verify async calls
            self.mock_client.scans.upload.start.assert_called_once()
            self.mock_client.scans.upload.file.add.assert_called_once()
            self.mock_client.scans.upload.file.complete.assert_called_once()
            self.mock_client.scans.upload.complete_all.assert_called_once()
            self.mock_client.scans.jobs.retrieve.assert_called_once()

            assert result is mock_scan_report

        finally:
            # Clean up temp file
            os.unlink(temp_path)


class TestFilterPathObjects:
    """Test the filter_path_objects utility function."""

    def test_filter_with_allow_patterns(self) -> None:
        """Test filtering with allow patterns."""
        test_files: list[PathInputType] = [
            Path("model.pkl"),
            Path("config.json"),
            Path("weights.pt"),
            Path("readme.txt"),
        ]

        filtered = list(filter_path_objects(test_files, allow_patterns=["*.pkl", "*.pt"]))

        names = [Path(f).name for f in filtered]
        assert "model.pkl" in names
        assert "weights.pt" in names
        assert "config.json" not in names
        assert "readme.txt" not in names

    def test_filter_with_ignore_patterns(self) -> None:
        """Test filtering with ignore patterns."""
        test_files: list[PathInputType] = [Path("model.pkl"), Path("config.json"), Path("readme.txt"), Path("data.md")]

        filtered = list(filter_path_objects(test_files, ignore_patterns=["*.txt", "*.md"]))

        names = [Path(f).name for f in filtered]
        assert "model.pkl" in names
        assert "config.json" in names
        assert "readme.txt" not in names
        assert "data.md" not in names

    def test_filter_with_exclude_file_types(self) -> None:
        """Test filtering with default EXCLUDE_FILE_TYPES."""
        test_files: list[PathInputType] = [
            Path("model.pkl"),
            Path("config.json"),
            Path("readme.txt"),  # Should be excluded
            Path("docs.md"),  # Should be excluded
            Path("package.lock"),  # Should be excluded
        ]

        filtered = list(filter_path_objects(test_files, ignore_patterns=EXCLUDE_FILE_TYPES))

        names = [Path(f).name for f in filtered]
        assert "model.pkl" in names
        assert "config.json" in names
        assert "readme.txt" not in names
        assert "docs.md" not in names
        assert "package.lock" not in names

    def test_filter_empty_input(self) -> None:
        """Test filtering with empty input."""
        filtered = list(filter_path_objects([]))
        assert len(filtered) == 0

    def test_filter_no_patterns(self) -> None:
        """Test filtering with no patterns (should include all)."""
        test_files: list[PathInputType] = [Path("model.pkl"), Path("config.json")]
        filtered = list(filter_path_objects(test_files))
        assert len(filtered) == 2


class TestScanStatus:
    """Test ScanStatus constants."""

    def test_scan_status_constants(self) -> None:
        """Test that ScanStatus constants are defined correctly."""
        assert ScanStatus.DONE == "done"
        assert ScanStatus.FAILED == "failed"
        assert ScanStatus.PENDING == "pending"
        assert ScanStatus.RUNNING == "running"
        assert ScanStatus.CANCELED == "canceled"


class TestExcludeFileTypes:
    """Test EXCLUDE_FILE_TYPES constant."""

    def test_exclude_file_types_constant(self) -> None:
        """Test that EXCLUDE_FILE_TYPES contains expected patterns."""
        expected_patterns = [
            "*.txt",
            "*.md",
            "*.lock",
            ".gitattributes",
            ".git",
            ".git/*",
            "*/.git",
            "**/.git/**",
        ]

        for pattern in expected_patterns:
            assert pattern in EXCLUDE_FILE_TYPES
