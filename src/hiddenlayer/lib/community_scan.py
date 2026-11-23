"""Community scans: models the HiddenLayer Model Scanner fetches from a remote location itself."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Literal, Union

from ..scans.jobs.types.scan_job_request_access import ScanJobRequestAccess
from ..types.scan_job_inventory import ScanJobInventory
from .scan_utils import (
    AsyncScanResultMixin,
    ScanReport,
    ScanResultMixin,
    get_scan_results,
    get_scan_results_async,
    wait_for_scan_results,
    wait_for_scan_results_async,
)

if TYPE_CHECKING:
    from ..client import AsyncHiddenLayer, HiddenLayer

logger = logging.getLogger(__name__)

REQUESTING_ENTITY = "hiddenlayer-python-sdk"

ModelSource = Union[
    str,
    Literal[
        "LOCAL",
        "AWS_PRESIGNED",
        "AWS_IAM_ROLE",
        "AZURE_BLOB_SAS",
        "AZURE_BLOB_AD",
        "GOOGLE_SIGNED",
        "GOOGLE_OAUTH",
        "HUGGING_FACE",
    ],
]


class CommunityScanSource:
    """The remote locations a community scan can read a model from."""

    LOCAL = "LOCAL"
    AWS_PRESIGNED = "AWS_PRESIGNED"
    AWS_IAM_ROLE = "AWS_IAM_ROLE"
    AZURE_BLOB_SAS = "AZURE_BLOB_SAS"
    AZURE_BLOB_AD = "AZURE_BLOB_AD"
    GOOGLE_SIGNED = "GOOGLE_SIGNED"
    GOOGLE_OAUTH = "GOOGLE_OAUTH"
    HUGGING_FACE = "HUGGING_FACE"


def _inventory(
    *, model_name: str, model_version: str, model_path: str, request_source: str, origin: str
) -> ScanJobInventory:
    return ScanJobInventory(
        model_name=model_name,
        model_version=model_version,
        requested_scan_location=model_path,
        requesting_entity=REQUESTING_ENTITY,
        request_source=request_source,
        origin=origin,
    )


class CommunityScanner(ScanResultMixin):
    """Requests a scan of a model at a remote location and returns its report."""

    def __init__(self, client: "HiddenLayer") -> None:
        self._client = client

    def community_scan(
        self,
        model_name: str,
        model_path: str,
        model_source: ModelSource,
        model_version: str = "main",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> ScanReport:
        """Scans a model at a remote location with the HiddenLayer Model Scanner.

        Args:
            model_name: Name of the model, as shown in the HiddenLayer Console.
            model_path: Where the model is, e.g. a presigned S3 URL.
            model_source: The kind of location model_path is; see CommunityScanSource.
            model_version: Version of the model, as shown in the HiddenLayer Console.
            wait_for_results: Whether to wait for the scan to finish. When False, the report is
                returned as it stands.
            request_source: What requested the scan.
            origin: The platform the model came from.

        Raises:
            ValueError: If the API returns a scan job with no scan ID.
        """
        scan_job = self._client.scans.jobs.request(
            access=ScanJobRequestAccess(source=model_source),
            inventory=_inventory(
                model_name=model_name,
                model_version=model_version,
                model_path=model_path,
                request_source=request_source,
                origin=origin,
            ),
        )
        scan_id = scan_job.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        if wait_for_results:
            return wait_for_scan_results(self._client, scan_id=scan_id)
        return get_scan_results(self._client, scan_id=scan_id)


class AsyncCommunityScanner(AsyncScanResultMixin):
    """Async version of CommunityScanner, for AsyncHiddenLayer."""

    def __init__(self, client: "AsyncHiddenLayer") -> None:
        self._client = client

    async def community_scan(
        self,
        model_name: str,
        model_path: str,
        model_source: ModelSource,
        model_version: str = "main",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> ScanReport:
        """Async version of CommunityScanner.community_scan."""
        scan_job = await self._client.scans.jobs.request(
            access=ScanJobRequestAccess(source=model_source),
            inventory=_inventory(
                model_name=model_name,
                model_version=model_version,
                model_path=model_path,
                request_source=request_source,
                origin=origin,
            ),
        )
        scan_id = scan_job.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        if wait_for_results:
            return await wait_for_scan_results_async(self._client, scan_id=scan_id)
        return await get_scan_results_async(self._client, scan_id=scan_id)
