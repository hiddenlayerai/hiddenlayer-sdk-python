from datetime import datetime
from typing import List, Optional

from pydantic import StrictStr
from typing_extensions import Self

from hiddenlayer.sdk.constants import ScanStatus
from hiddenlayer.sdk.rest.models import (
    ModelInventoryInfo,
    ScanReportV3,
)
from hiddenlayer.sdk.rest.models.file_scan_report_v3 import FileScanReportV3
from hiddenlayer.sdk.rest.models.sarif210 import Sarif210


class ScanResults(ScanReportV3):
    """This class exists because the ScanResults API doesn't return anything about the file name or path that was scanned."""

    file_name: Optional[str] = None
    file_path: Optional[str] = None

    @classmethod
    def from_scanreportv3(
        cls, *, scan_report_v3: ScanReportV3, model_id: Optional[str] = None
    ) -> Self:
        scan_results_dict = scan_report_v3.to_dict()
        result = cls(**scan_results_dict)

        return result


class EmptyScanResults(ScanResults):
    status: str = ScanStatus.PENDING
    file_count: int = 0
    files_with_detections_count: int = 0
    detection_count: int = 0
    detection_categories: Optional[List[StrictStr]] = []
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
    end_time: Optional[datetime] = datetime.now()
    severity: Optional[StrictStr] = ""
    file_results: Optional[List[FileScanReportV3]] = []


class Sarif(Sarif210):
    """This class exists because the generated code for Sarif210 treats version as a Dictionary which it is not."""

    version: str  # type: ignore
