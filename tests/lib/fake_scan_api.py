"""An in-memory stand-in for the scan API and the presigned upload host, answering through httpx.MockTransport."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Sequence, Union

import httpx

API_URL = "https://api.hiddenlayer.test"
UPLOAD_URL = "https://uploads.hiddenlayer.test"
SCAN_ID = "5f1d6a8e-3c2b-4e7a-9d1f-0a2b3c4d5e6f"
NOT_FOUND = 404
TIMED_OUT = 0


def file_result(name: str) -> Dict[str, Any]:
    return {
        "file_instance_id": f"instance-{name}",
        "file_location": name,
        "start_time": "2026-03-02T10:15:00Z",
        "end_time": "2026-03-02T10:15:04Z",
        "seen": "2026-03-02T10:15:04Z",
        "status": "done",
        "details": {"estimated_time": "4s", "sha256": "9f86d081884c7d65", "file_type": "pickle"},
        "detections": [],
    }


class FakeScanApi:
    """Serves one scan: the upload, the scan job, the summary and the paginated file results.

    Args:
        summaries: What the summary endpoint answers, call by call, as a scan status, 404 or
            TIMED_OUT, a request that times out; the last one repeats.
        files: File names the files endpoint lists, a page at a time.
        part_size: Bytes per presigned upload part.
        duplicate_files: File names the API refuses as already uploaded.
        rejected_files: File names the API refuses for another reason.
        summary_fields: Fields added to every summary.
    """

    def __init__(
        self,
        *,
        summaries: Sequence[Union[str, int]] = ("done",),
        files: Sequence[str] = ("model.pkl",),
        part_size: int = 4,
        duplicate_files: Sequence[str] = (),
        rejected_files: Sequence[str] = (),
        summary_fields: Optional[Dict[str, Any]] = None,
    ) -> None:
        self._summaries = list(summaries)
        self._files = list(files)
        self._part_size = part_size
        self._duplicate_files = set(duplicate_files)
        self._rejected_files = set(rejected_files)
        self._summary_fields = summary_fields or {}
        self.requests: List[httpx.Request] = []
        self.uploaded: Dict[str, bytes] = {}
        self.upload_status = 200
        self.scan_job_response: Dict[str, Any] = {
            "scan_id": SCAN_ID,
            "status": "pending",
            "inventory": {
                "model_name": "sentiment-classifier",
                "model_version": "main",
                "requesting_entity": "hiddenlayer-python-sdk",
            },
        }
        self.omit_upload_url = False

    @property
    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self._handle)

    def calls(self, method: str, path: str) -> List[httpx.Request]:
        return [request for request in self.requests if request.method == method and request.url.path == path]

    def body(self, method: str, path: str) -> Dict[str, Any]:
        (request,) = self.calls(method, path)
        body: Dict[str, Any] = json.loads(request.content)
        return body

    def _handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if str(request.url).startswith(UPLOAD_URL):
            self.uploaded[request.url.path] = request.content
            return httpx.Response(self.upload_status)

        path, method = request.url.path, request.method
        upload = f"/scan/v3/upload/{SCAN_ID}"
        if (method, path) == ("POST", "/scan/v3/upload"):
            return httpx.Response(200, json={"scan_id": SCAN_ID})
        if (method, path) == ("POST", f"{upload}/file"):
            return self._add_file(request)
        if method == "PATCH" and path.startswith(f"{upload}/file/"):
            return httpx.Response(200, json={"scan_id": SCAN_ID})
        if (method, path) == ("PATCH", upload):
            return httpx.Response(200, json={"scan_id": SCAN_ID})
        if (method, path) == ("POST", "/scan/v3/jobs"):
            return httpx.Response(201, json=self.scan_job_response)
        if (method, path) == ("GET", f"/scan/v3/results/{SCAN_ID}/summary"):
            return self._summary()
        if (method, path) == ("GET", f"/scan/v3/results/{SCAN_ID}/files"):
            return self._file_results(request)
        return httpx.Response(404, json={"detail": f"no route for {method} {path}"})

    def _add_file(self, request: httpx.Request) -> httpx.Response:
        name = request.headers["file-name"].rsplit("/", 1)[-1]
        if name in self._duplicate_files:
            return httpx.Response(400, json={"detail": "Duplicate file detected in scan"})
        if name in self._rejected_files:
            return httpx.Response(400, json={"detail": "File name is not allowed"})
        length = int(request.headers["file-content-length"])
        upload_id = f"upload-{len(self.calls('POST', request.url.path))}"
        offsets = range(0, max(length, 1), self._part_size)
        parts = [
            {
                "part_number": number,
                "start_offset": start,
                "end_offset": min(start + self._part_size, length),
                "upload_url": None if self.omit_upload_url else f"{UPLOAD_URL}/{upload_id}/{number}",
            }
            for number, start in enumerate(offsets, start=1)
        ]
        return httpx.Response(200, json={"upload_id": upload_id, "parts": parts})

    def _summary(self) -> httpx.Response:
        answer = self._summaries.pop(0) if len(self._summaries) > 1 else self._summaries[0]
        if answer == NOT_FOUND:
            return httpx.Response(404, json={"detail": "scan not found"})
        if answer == TIMED_OUT:
            raise httpx.ReadTimeout("The read operation timed out")
        return httpx.Response(
            200,
            json={
                "scan_id": SCAN_ID,
                "status": answer,
                "version": "25.11.0",
                "start_time": "2026-03-02T10:15:00Z",
                "$schema_version": "3.2.0",
                "inventory": {
                    "model_id": "0b6f1c1e-model",
                    "model_version_id": "7a3e9d42-version",
                    "model_name": "sentiment-classifier",
                    "requested_scan_location": "model.pkl",
                },
                "summary": {
                    "detection_count": 3,
                    "file_count": len(self._files),
                    "files_with_detections_count": 2,
                    "detection_categories": ["Arbitrary Code Execution"],
                    "severity": "high",
                },
                **self._summary_fields,
            },
        )

    def _file_results(self, request: httpx.Request) -> httpx.Response:
        page_size = int(request.url.params["page_size"])
        start = int(request.url.params.get("cursor", "0"))
        end = start + page_size
        return httpx.Response(
            200,
            json={
                "items": [file_result(name) for name in self._files[start:end]],
                "first": "0",
                "prev": "",
                "next": str(end) if end < len(self._files) else "",
            },
        )
