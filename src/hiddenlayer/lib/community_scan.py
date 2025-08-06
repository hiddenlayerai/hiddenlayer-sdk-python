"""
Community scan functionality for Hidden Layer SDK.

This module provides the community_scan method that was available in the old SDK,
which combines scan request + polling + results retrieval in a single convenient method.
"""

import logging
from typing import Union, Literal, cast
from typing_extensions import TYPE_CHECKING

from .scan_utils import get_scan_results, wait_for_scan_results, get_scan_results_async, wait_for_scan_results_async

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from .. import HiddenLayer, AsyncHiddenLayer
    from ..types.scans import ScanReport


class CommunityScanSource:
    """Community scan source constants matching the old SDK."""

    LOCAL = "LOCAL"
    AWS_PRESIGNED = "AWS_PRESIGNED"
    AWS_IAM_ROLE = "AWS_IAM_ROLE"
    AZURE_BLOB_SAS = "AZURE_BLOB_SAS"
    AZURE_BLOB_AD = "AZURE_BLOB_AD"
    GOOGLE_SIGNED = "GOOGLE_SIGNED"
    GOOGLE_OAUTH = "GOOGLE_OAUTH"
    HUGGING_FACE = "HUGGING_FACE"


class CommunityScanner:
    """
    Community scanner that provides the community_scan method with polling functionality.

    This class extends the generated SDK to provide the same functionality as the old SDK's
    community_scan method, which initiates a scan and optionally waits for results.
    """

    def __init__(self, client: "HiddenLayer") -> None:
        self._client = client

    def community_scan(
        self,
        model_name: str,
        model_path: str,
        model_source: Union[
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
        ],
        model_version: str = "main",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> "ScanReport":
        """
        Scan a model available at a remote location using the HiddenLayer Model Scanner.

        :param model_name: Name of the model to be shown on the HiddenLayer UI.
        :param model_path: Path to the model file in the remote location, e.g. a presigned S3 URL
        :param model_source: type of remote location where the model is stored.
        :param model_version: Version of the model to be shown on the HiddenLayer UI.
        :param wait_for_results: True whether to wait for the scan to finish, defaults to True.
        :param request_source: Source that requested the scan.
        :param origin: Origin platform where the model came from.

        :returns: Scan Results
        """
        # Create the scan job
        scan_job = self._client.scans.jobs.request(
            access={
                "source": cast(
                    "Literal['LOCAL', 'AWS_PRESIGNED', 'AWS_IAM_ROLE', 'AZURE_BLOB_SAS', 'AZURE_BLOB_AD', 'GOOGLE_SIGNED', 'GOOGLE_OAUTH', 'HUGGING_FACE']",
                    model_source,
                )
            },
            inventory={
                "model_name": model_name,
                "model_version": model_version,
                "requested_scan_location": model_path,
                "requesting_entity": "hiddenlayer-python-sdk",
                "request_source": cast(
                    "Literal['Hybrid Upload', 'API Upload', 'Integration', 'UI Upload']", request_source
                ),
                "origin": origin,
            },
        )

        scan_id = scan_job.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        if wait_for_results:
            return wait_for_scan_results(self._client, scan_id=scan_id)
        else:
            # Return current scan status without waiting
            return get_scan_results(self._client, scan_id=scan_id)


class AsyncCommunityScanner:
    """
    Async version of CommunityScanner for use with AsyncHiddenLayer client.
    """

    def __init__(self, client: "AsyncHiddenLayer") -> None:
        self._client = client

    async def community_scan(
        self,
        model_name: str,
        model_path: str,
        model_source: Union[
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
        ],
        model_version: str = "main",
        wait_for_results: bool = True,
        request_source: str = "API Upload",
        origin: str = "",
    ) -> "ScanReport":
        """
        Async version of community_scan.

        See CommunityScanner.community_scan for parameter documentation.
        """
        # Create the scan job
        scan_job = await self._client.scans.jobs.request(
            access={
                "source": cast(
                    "Literal['LOCAL', 'AWS_PRESIGNED', 'AWS_IAM_ROLE', 'AZURE_BLOB_SAS', 'AZURE_BLOB_AD', 'GOOGLE_SIGNED', 'GOOGLE_OAUTH', 'HUGGING_FACE']",
                    model_source,
                )
            },
            inventory={
                "model_name": model_name,
                "model_version": model_version,
                "requested_scan_location": model_path,
                "requesting_entity": "hiddenlayer-python-sdk",
                "request_source": cast(
                    "Literal['Hybrid Upload', 'API Upload', 'Integration', 'UI Upload']", request_source
                ),
                "origin": origin,
            },
        )

        scan_id = scan_job.scan_id
        if scan_id is None:
            raise ValueError("scan_id must have a value")

        if wait_for_results:
            return await wait_for_scan_results_async(self._client, scan_id=scan_id)
        else:
            # Return current scan status without waiting
            return await get_scan_results_async(self._client, scan_id=scan_id)
