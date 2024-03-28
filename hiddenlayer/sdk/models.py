from typing import Optional

from typing_extensions import Self

from hiddenlayer.sdk.rest.models import ScanResultsV2


class ScanResults(ScanResultsV2):
    """This class exists because the ScanResults API doesn't return anything about the file name or path that was scanned."""

    file_name: Optional[str] = None
    file_path: Optional[str] = None
    sensor_id: Optional[str] = None

    @classmethod
    def from_scanresultsv2(
        cls, *, scan_results_v2: ScanResultsV2, sensor_id: Optional[str] = None
    ) -> Self:
        scan_results_dict = scan_results_v2.to_dict()
        scan_results_dict["sensor_id"] = sensor_id

        return cls(**scan_results_dict)
