# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .scan_job import ScanJob

__all__ = ["JobListResponse"]

JobListResponse: TypeAlias = List[ScanJob]
