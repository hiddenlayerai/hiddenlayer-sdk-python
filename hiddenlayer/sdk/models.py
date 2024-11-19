from datetime import datetime
from typing import Optional

from pydantic import StrictStr
from typing_extensions import Self

from hiddenlayer.sdk.constants import ScanStatus
from hiddenlayer.sdk.rest.models import (
    FileScanReportV3,
    ModelInventoryInfo,
    ScanReportV3,
)
from hiddenlayer.sdk.rest.models.file_results_inner import FileResultsInner


class ScanResults(ScanReportV3):
    """This class exists because the ScanResults API doesn't return anything about the file name or path that was scanned."""

    file_name: Optional[str] = None
    file_path: Optional[str] = None
    model_id: Optional[str] = None

    @classmethod
    def from_scanreportv3(
        cls, *, scan_report_v3: ScanReportV3, model_id: Optional[str] = None
    ) -> Self:
        scan_results_dict = scan_report_v3.to_dict()
        scan_results_dict["model_id"] = model_id

        return cls(**scan_results_dict)


class EmptyScanResults(ScanResults):
    status: str = ScanStatus.PENDING
    file_count: int = 0
    files_with_detections_count: int = 0
    detection_count: int = 0
    detection_categories: list[StrictStr] | None = []
    inventory: ModelInventoryInfo = ModelInventoryInfo(
        model_name="",
        model_version="",
        model_source="",
        requested_scan_location="",
        requesting_entity="",
        model_id="",
        model_version_id="",
    )
    version: str = ""
    scan_id: str = ""
    start_time: datetime = datetime.now()
    end_time: datetime | None = datetime.now()
    severity: StrictStr | None = ""
    file_results: list[FileResultsInner] | None = []
