from typing import Optional

from typing_extensions import Self

from hiddenlayer.rest.models import ScanResultsV2


class ScanResults(ScanResultsV2):
    """This class exists because the ScanResults API doesn't return anything about the file name or path that was scanned."""

    file_name: Optional[str] = None
    file_path: Optional[str] = None

    @classmethod
    def from_scanresultsv2(cls, *, scan_results_v2: ScanResultsV2) -> Self:
        return cls(**scan_results_v2.to_dict())
