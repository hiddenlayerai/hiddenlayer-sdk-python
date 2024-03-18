import pytest

from pathlib import Path

from hiddenlayer.utils import filter_path_objects


@pytest.fixture(scope="class")
def paths():
    return [Path("/tmp/test.txt"), Path("/tmp/test.xgb"), Path("/tmp/test.pkl")]


@pytest.fixture(scope="class", autouse=True)
def create_temp_files(paths):
    for path in paths:
        path.touch()

    yield

    for path in paths:
        path.unlink()


def test_filter_path_ignore_list(paths):
    """Test to correctly filter paths with ignore list"""
    filtered_paths = list(filter_path_objects(paths, ignore_patterns=["*.txt"]))

    assert filtered_paths == [Path("/tmp/test.xgb"), Path("/tmp/test.pkl")]


def test_filter_paths_allow_list(paths):
    """Test to correctly filter paths with ignore list"""
    filtered_paths = list(filter_path_objects(paths, allow_patterns=["*.xgb"]))

    assert filtered_paths == [Path("/tmp/test.xgb")]
