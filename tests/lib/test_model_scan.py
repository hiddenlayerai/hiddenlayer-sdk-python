from __future__ import annotations

import os
import shutil
import sys
import uuid
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, Iterator, List, Optional

import httpx
import pytest
from fake_scan_api import API_URL, SCAN_ID, UPLOAD_URL, FakeScanApi

from hiddenlayer import AsyncHiddenLayer, HiddenLayer
from hiddenlayer.errors import BadRequestError
from hiddenlayer.lib import scan_utils
from hiddenlayer.lib.model_scan import EXCLUDE_FILE_TYPES, PathInputType, filter_path_objects, is_duplicate_file_error

START_PATH = "/scan/v3/upload"
ADD_FILE_PATH = f"/scan/v3/upload/{SCAN_ID}/file"
COMPLETE_ALL_PATH = f"/scan/v3/upload/{SCAN_ID}"
MODEL_BYTES = b"0123456789"


def sync_client(api: FakeScanApi) -> HiddenLayer:
    return HiddenLayer(
        token="test-token", base_url=API_URL, httpx_client=httpx.Client(transport=api.transport), max_retries=0
    )


def async_client(api: FakeScanApi) -> AsyncHiddenLayer:
    return AsyncHiddenLayer(
        token="test-token", base_url=API_URL, httpx_client=httpx.AsyncClient(transport=api.transport), max_retries=0
    )


def uploaded_names(api: FakeScanApi) -> List[str]:
    return sorted(request.headers["file-name"] for request in api.calls("POST", ADD_FILE_PATH))


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    async def skip(delay: float) -> None:
        return None

    monkeypatch.setattr(scan_utils.time, "sleep", lambda delay: None)
    monkeypatch.setattr(scan_utils.asyncio, "sleep", skip)


@pytest.fixture
def model_file(tmp_path: Path) -> Path:
    path = tmp_path / "model.pkl"
    path.write_bytes(MODEL_BYTES)
    return path


@pytest.fixture
def model_folder(tmp_path: Path) -> Path:
    folder = tmp_path / "sentiment-classifier"
    (folder / "nested").mkdir(parents=True)
    (folder / ".git").mkdir()
    (folder / "model.pkl").write_bytes(MODEL_BYTES)
    (folder / "nested" / "weights.bin").write_bytes(b"weights")
    (folder / "README.md").write_text("# Sentiment classifier")
    (folder / "notes.txt").write_text("trained 2026-02-11")
    (folder / "poetry.lock").write_text("")
    (folder / ".git" / "config").write_text("[core]")
    return folder


@pytest.fixture
def tmp_name() -> Iterator[str]:
    """A file or folder name the S3, Azure and Hugging Face scans download to under /tmp, removed afterwards."""
    name = f"hiddenlayer-sdk-test-{uuid.uuid4().hex}"
    yield name
    path = Path("/tmp") / name
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


class FakeS3Client:
    def __init__(self, content: Optional[bytes]) -> None:
        self._content = content
        self.downloads: List[Dict[str, str]] = []

    def download_file(self, bucket: str, key: str, filename: str) -> None:
        if self._content is None:
            raise PermissionError("Access Denied")
        self.downloads.append({"bucket": bucket, "key": key})
        Path(filename).write_bytes(self._content)


class FakeBlobServiceClient:
    def __init__(self, content: Optional[bytes]) -> None:
        self._content = content
        self.requested: List[Dict[str, str]] = []

    def get_blob_client(self, *, container: str, blob: str) -> "FakeBlobServiceClient":
        self.requested.append({"container": container, "blob": blob})
        return self

    def download_blob(self) -> "FakeBlobServiceClient":
        if self._content is None:
            raise PermissionError("AuthorizationFailure")
        return self

    def readall(self) -> bytes:
        assert self._content is not None
        return self._content


def install_module(monkeypatch: pytest.MonkeyPatch, name: str, **attributes: Any) -> None:
    module = ModuleType(name)
    for attribute, value in attributes.items():
        setattr(module, attribute, value)
    monkeypatch.setitem(sys.modules, name, module)


def install_azure(monkeypatch: pytest.MonkeyPatch) -> None:
    install_module(monkeypatch, "azure")
    install_module(monkeypatch, "azure.identity", DefaultAzureCredential=object)
    install_module(monkeypatch, "azure.storage")
    install_module(monkeypatch, "azure.storage.blob", BlobServiceClient=object)


def test_scan_file_uploads_the_file_in_parts_then_returns_the_report(model_file: Path) -> None:
    api = FakeScanApi(part_size=4)

    report = sync_client(api).model_scanner.scan_file(model_name="sentiment-classifier", model_path=model_file)

    assert api.body("POST", START_PATH) == {
        "model_name": "sentiment-classifier",
        "model_version": "1",
        "requesting_entity": "hiddenlayer-python-sdk",
        "request_source": "API Upload",
        "origin": "",
    }
    (add_file,) = api.calls("POST", ADD_FILE_PATH)
    assert add_file.headers["file-name"] == str(model_file)
    assert add_file.headers["file-content-length"] == "10"
    assert api.uploaded == {"/upload-1/1": b"0123", "/upload-1/2": b"4567", "/upload-1/3": b"89"}
    assert len(api.calls("PATCH", f"{ADD_FILE_PATH}/upload-1")) == 1
    assert len(api.calls("PATCH", COMPLETE_ALL_PATH)) == 1
    assert report.scan_id == SCAN_ID
    assert report.status == "done"


def test_presigned_uploads_carry_no_api_credentials(model_file: Path) -> None:
    api = FakeScanApi()

    sync_client(api).model_scanner.scan_file(model_name="sentiment-classifier", model_path=model_file)

    uploads = [request for request in api.requests if str(request.url).startswith(UPLOAD_URL)]
    assert len(uploads) == 3
    for upload in uploads:
        assert "authorization" not in upload.headers
        assert upload.headers["content-type"] == "application/octet-stream"


def test_scan_file_passes_the_version_request_source_and_origin(model_file: Path) -> None:
    api = FakeScanApi()

    sync_client(api).model_scanner.scan_file(
        model_name="sentiment-classifier",
        model_path=str(model_file),
        model_version="2026.03",
        request_source="Integration",
        origin="github-action",
    )

    body = api.body("POST", START_PATH)
    assert (body["model_version"], body["request_source"], body["origin"]) == (
        "2026.03",
        "Integration",
        "github-action",
    )


def test_scan_file_without_waiting_returns_the_report_as_it_stands(model_file: Path) -> None:
    api = FakeScanApi(summaries=["running"])

    report = sync_client(api).model_scanner.scan_file(
        model_name="sentiment-classifier", model_path=model_file, wait_for_results=False
    )

    assert report.status == "running"
    assert len(api.calls("GET", f"/scan/v3/results/{SCAN_ID}/summary")) == 1


def test_scan_file_stops_when_a_part_has_no_upload_url(model_file: Path) -> None:
    api = FakeScanApi()
    api.omit_upload_url = True

    with pytest.raises(ValueError, match="upload_url"):
        sync_client(api).model_scanner.scan_file(model_name="sentiment-classifier", model_path=model_file)

    assert api.calls("PATCH", COMPLETE_ALL_PATH) == []


def test_scan_file_raises_when_a_presigned_upload_is_refused(model_file: Path) -> None:
    api = FakeScanApi()
    api.upload_status = 403

    with pytest.raises(httpx.HTTPStatusError) as raised:
        sync_client(api).model_scanner.scan_file(model_name="sentiment-classifier", model_path=model_file)

    assert raised.value.response.status_code == 403
    assert api.calls("PATCH", COMPLETE_ALL_PATH) == []


def test_scan_result_returns_the_report_of_an_earlier_scan() -> None:
    report = sync_client(FakeScanApi(summaries=["failed"])).model_scanner.scan_result(scan_id=SCAN_ID)

    assert report.status == "failed"


def test_scan_folder_uploads_each_model_file_once_and_leaves_out_the_excluded_types(model_folder: Path) -> None:
    (model_folder / "latest.pkl").symlink_to(model_folder / "model.pkl")
    api = FakeScanApi()

    report = sync_client(api).model_scanner.scan_folder(model_name="sentiment-classifier", path=model_folder)

    names = uploaded_names(api)
    assert str(model_folder / "nested" / "weights.bin") in names
    assert len(names) == 2
    assert {os.path.realpath(name) for name in names} == {
        os.path.realpath(model_folder / "model.pkl"),
        os.path.realpath(model_folder / "nested" / "weights.bin"),
    }
    assert len(api.calls("PATCH", COMPLETE_ALL_PATH)) == 1
    assert report.status == "done"


def test_scan_folder_applies_the_allow_and_ignore_patterns(model_folder: Path) -> None:
    (model_folder / "tokenizer.json").write_text("{}")
    api = FakeScanApi()

    sync_client(api).model_scanner.scan_folder(
        model_name="sentiment-classifier",
        path=str(model_folder),
        allow_file_patterns=["*.pkl", "*.bin"],
        ignore_file_patterns=["*weights*"],
    )

    assert uploaded_names(api) == [str(model_folder / "model.pkl")]


def test_scan_folder_skips_a_file_the_scan_already_has(model_folder: Path) -> None:
    api = FakeScanApi(duplicate_files=["model.pkl"])

    report = sync_client(api).model_scanner.scan_folder(model_name="sentiment-classifier", path=model_folder)

    assert b"".join(api.uploaded[part] for part in sorted(api.uploaded)) == b"weights"
    assert len(api.calls("PATCH", COMPLETE_ALL_PATH)) == 1
    assert report.status == "done"


def test_scan_folder_raises_any_other_bad_request(model_folder: Path) -> None:
    api = FakeScanApi(rejected_files=["model.pkl"])

    with pytest.raises(BadRequestError) as raised:
        sync_client(api).model_scanner.scan_folder(model_name="sentiment-classifier", path=model_folder)

    assert raised.value.body == {"detail": "File name is not allowed"}
    assert api.calls("PATCH", COMPLETE_ALL_PATH) == []


def test_scan_s3_model_downloads_the_object_with_the_default_client_then_scans_it(
    monkeypatch: pytest.MonkeyPatch, tmp_name: str
) -> None:
    s3_client = FakeS3Client(MODEL_BYTES)
    install_module(monkeypatch, "boto3", client=lambda service: s3_client)
    api = FakeScanApi(part_size=16)

    report = sync_client(api).model_scanner.scan_s3_model(
        model_name="sentiment-classifier", bucket="acme-models", key=f"release/{tmp_name}"
    )

    assert s3_client.downloads == [{"bucket": "acme-models", "key": f"release/{tmp_name}"}]
    assert api.body("POST", START_PATH)["origin"] == "S3"
    assert uploaded_names(api) == [f"/tmp/{tmp_name}"]
    assert api.uploaded == {"/upload-1/1": MODEL_BYTES}
    assert report.status == "done"


def test_scan_s3_model_reports_a_failed_download_without_starting_a_scan(monkeypatch: pytest.MonkeyPatch) -> None:
    install_module(monkeypatch, "boto3")
    api = FakeScanApi()

    with pytest.raises(RuntimeError, match="s3://acme-models/release/model.pkl: Access Denied"):
        sync_client(api).model_scanner.scan_s3_model(
            model_name="sentiment-classifier",
            bucket="acme-models",
            key="release/model.pkl",
            s3_client=FakeS3Client(None),
        )

    assert api.requests == []


def test_scan_s3_model_needs_boto3(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "boto3", None)

    with pytest.raises(ImportError, match="boto3 is not installed"):
        sync_client(FakeScanApi()).model_scanner.scan_s3_model(
            model_name="sentiment-classifier", bucket="acme-models", key="release/model.pkl"
        )


def test_scan_azure_blob_model_downloads_the_blob_then_scans_it(monkeypatch: pytest.MonkeyPatch, tmp_name: str) -> None:
    install_azure(monkeypatch)
    blob_service_client = FakeBlobServiceClient(MODEL_BYTES)
    api = FakeScanApi(part_size=16)

    report = sync_client(api).model_scanner.scan_azure_blob_model(
        model_name="sentiment-classifier",
        account_url="https://acmemodels.blob.core.windows.net",
        container="release",
        blob=f"2026/{tmp_name}",
        blob_service_client=blob_service_client,
    )

    assert blob_service_client.requested == [{"container": "release", "blob": f"2026/{tmp_name}"}]
    assert api.body("POST", START_PATH)["origin"] == "Azure Blob Storage"
    assert uploaded_names(api) == [f"/tmp/{tmp_name}"]
    assert api.uploaded == {"/upload-1/1": MODEL_BYTES}
    assert report.status == "done"


def test_scan_azure_blob_model_reports_a_failed_download_without_starting_a_scan(
    monkeypatch: pytest.MonkeyPatch, tmp_name: str
) -> None:
    install_azure(monkeypatch)
    api = FakeScanApi()

    with pytest.raises(RuntimeError, match="Couldn't download model https://acmemodels.blob.core.windows.net"):
        sync_client(api).model_scanner.scan_azure_blob_model(
            model_name="sentiment-classifier",
            account_url="https://acmemodels.blob.core.windows.net",
            container="release",
            blob=f"2026/{tmp_name}",
            blob_service_client=FakeBlobServiceClient(None),
        )

    assert api.requests == []


def test_scan_azure_blob_model_needs_the_azure_packages(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "azure.identity", None)

    with pytest.raises(ImportError, match="azure-identity is not installed"):
        sync_client(FakeScanApi()).model_scanner.scan_azure_blob_model(
            model_name="sentiment-classifier",
            account_url="https://acmemodels.blob.core.windows.net",
            container="release",
            blob="2026/model.pkl",
        )


def test_scan_huggingface_model_downloads_the_repository_then_scans_the_folder(
    monkeypatch: pytest.MonkeyPatch, tmp_name: str
) -> None:
    downloads: List[Dict[str, Any]] = []

    def snapshot_download(repo_id: str, **options: Any) -> None:
        downloads.append({"repo_id": repo_id, **options})
        Path(options["local_dir"]).mkdir(parents=True)
        (Path(options["local_dir"]) / "model.safetensors").write_bytes(MODEL_BYTES)
        (Path(options["local_dir"]) / "README.md").write_text("# Model card")

    install_module(monkeypatch, "huggingface_hub", snapshot_download=snapshot_download)
    api = FakeScanApi(part_size=16)

    report = sync_client(api).model_scanner.scan_huggingface_model(
        repo_id=tmp_name, ignore_file_patterns=["*.onnx"], hf_token="hf_test_token"
    )

    assert downloads == [
        {
            "repo_id": tmp_name,
            "revision": None,
            "allow_patterns": None,
            "ignore_patterns": EXCLUDE_FILE_TYPES + ["*.onnx"],
            "local_dir": f"/tmp/{tmp_name}",
            "local_dir_use_symlinks": False,
            "cache_dir": f"/tmp/{tmp_name}",
            "force_download": False,
            "token": "hf_test_token",
        }
    ]
    body = api.body("POST", START_PATH)
    assert (body["model_name"], body["model_version"], body["origin"]) == (tmp_name, "1", "Hugging Face")
    assert uploaded_names(api) == [f"/tmp/{tmp_name}/model.safetensors"]
    assert report.status == "done"


def test_scan_huggingface_model_uses_the_revision_as_the_model_version(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    install_module(monkeypatch, "huggingface_hub", snapshot_download=lambda repo_id, **options: None)
    api = FakeScanApi()

    sync_client(api).model_scanner.scan_huggingface_model(
        repo_id="acme/sentiment-classifier", model_name="sentiment", revision="v2.1", local_dir=str(tmp_path)
    )

    body = api.body("POST", START_PATH)
    assert (body["model_name"], body["model_version"]) == ("sentiment", "v2.1")


def test_scan_huggingface_model_needs_huggingface_hub(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "huggingface_hub", None)

    with pytest.raises(ImportError, match="huggingface_hub is not installed"):
        sync_client(FakeScanApi()).model_scanner.scan_huggingface_model(repo_id="acme/sentiment-classifier")


async def test_async_scan_file_uploads_the_file_in_parts_then_returns_the_report(model_file: Path) -> None:
    api = FakeScanApi(part_size=4)

    report = await async_client(api).model_scanner.scan_file(
        model_name="sentiment-classifier", model_path=model_file, origin="github-action"
    )

    assert api.body("POST", START_PATH)["origin"] == "github-action"
    assert api.uploaded == {"/upload-1/1": b"0123", "/upload-1/2": b"4567", "/upload-1/3": b"89"}
    assert len(api.calls("PATCH", f"{ADD_FILE_PATH}/upload-1")) == 1
    assert len(api.calls("PATCH", COMPLETE_ALL_PATH)) == 1
    assert report.status == "done"


async def test_async_presigned_uploads_carry_no_api_credentials(model_file: Path) -> None:
    api = FakeScanApi()

    await async_client(api).model_scanner.scan_file(model_name="sentiment-classifier", model_path=model_file)

    uploads = [request for request in api.requests if str(request.url).startswith(UPLOAD_URL)]
    assert len(uploads) == 3
    for upload in uploads:
        assert "authorization" not in upload.headers


async def test_async_scan_file_raises_when_a_presigned_upload_is_refused(model_file: Path) -> None:
    api = FakeScanApi()
    api.upload_status = 403

    with pytest.raises(httpx.HTTPStatusError) as raised:
        await async_client(api).model_scanner.scan_file(model_name="sentiment-classifier", model_path=model_file)

    assert raised.value.response.status_code == 403


async def test_async_scan_folder_skips_a_file_the_scan_already_has(model_folder: Path) -> None:
    api = FakeScanApi(duplicate_files=["model.pkl"])

    report = await async_client(api).model_scanner.scan_folder(
        model_name="sentiment-classifier", path=model_folder, wait_for_results=False
    )

    assert b"".join(api.uploaded[part] for part in sorted(api.uploaded)) == b"weights"
    assert len(api.calls("PATCH", COMPLETE_ALL_PATH)) == 1
    assert report.status == "done"


async def test_async_scan_folder_raises_any_other_bad_request(model_folder: Path) -> None:
    api = FakeScanApi(rejected_files=["weights.bin"])

    with pytest.raises(BadRequestError) as raised:
        await async_client(api).model_scanner.scan_folder(model_name="sentiment-classifier", path=model_folder)

    assert raised.value.body == {"detail": "File name is not allowed"}
    assert api.calls("PATCH", COMPLETE_ALL_PATH) == []


async def test_async_scan_s3_model_downloads_then_scans(monkeypatch: pytest.MonkeyPatch, tmp_name: str) -> None:
    install_module(monkeypatch, "boto3")
    api = FakeScanApi(part_size=16)

    await async_client(api).model_scanner.scan_s3_model(
        model_name="sentiment-classifier",
        bucket="acme-models",
        key=f"release/{tmp_name}",
        s3_client=FakeS3Client(MODEL_BYTES),
    )

    assert api.body("POST", START_PATH)["origin"] == "S3"
    assert api.uploaded == {"/upload-1/1": MODEL_BYTES}


@pytest.mark.parametrize(
    ("allow_patterns", "ignore_patterns", "expected"),
    [
        (None, None, ["model.pkl", "weights.bin", "notes.txt"]),
        ("*.pkl", None, ["model.pkl"]),
        (["*.pkl", "*.bin"], None, ["model.pkl", "weights.bin"]),
        (None, "*.txt", ["model.pkl", "weights.bin"]),
        (["*.pkl", "*.txt"], ["*notes*"], ["model.pkl"]),
        (None, EXCLUDE_FILE_TYPES, ["model.pkl", "weights.bin"]),
    ],
)
def test_filter_path_objects_applies_the_allowlist_then_the_denylist(
    tmp_path: Path, allow_patterns: Any, ignore_patterns: Any, expected: List[str]
) -> None:
    for name in ("model.pkl", "weights.bin", "notes.txt"):
        (tmp_path / name).write_bytes(b"x")
    (tmp_path / "checkpoints").mkdir()
    items: List[PathInputType] = [
        tmp_path / "model.pkl",
        str(tmp_path / "weights.bin"),
        tmp_path / "notes.txt",
        tmp_path / "checkpoints",
    ]

    kept = filter_path_objects(items, allow_patterns=allow_patterns, ignore_patterns=ignore_patterns)

    assert [Path(item).name for item in kept] == expected


def test_filter_path_objects_yields_a_file_once_however_it_is_reached(tmp_path: Path) -> None:
    (tmp_path / "model.pkl").write_bytes(b"x")
    (tmp_path / "latest.pkl").symlink_to(tmp_path / "model.pkl")

    kept = list(filter_path_objects([tmp_path / "model.pkl", tmp_path / "latest.pkl", tmp_path / "model.pkl"]))

    assert kept == [tmp_path / "model.pkl"]


def test_filter_path_objects_refuses_anything_but_a_str_or_a_path() -> None:
    with pytest.raises(ValueError, match="string or Pathlike"):
        list(filter_path_objects([b"model.pkl"]))  # type: ignore[list-item]


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        ({"detail": "Duplicate file detected in scan"}, True),
        ({"detail": "this file is a duplicate"}, True),
        ({"detail": "File name is not allowed"}, False),
        ({"detail": ["duplicate"]}, False),
        ({"title": "Bad Request"}, False),
        ("duplicate", False),
    ],
)
def test_is_duplicate_file_error_reads_the_detail_of_the_response_body(body: Any, expected: bool) -> None:
    assert is_duplicate_file_error(BadRequestError(body=body)) is expected
