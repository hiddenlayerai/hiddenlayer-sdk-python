from pathlib import Path

import pytest

from hiddenlayer.sdk.utils import filter_path_objects, is_saas


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


def test_is_saas():
    """Test if a url is our SaaS"""

    assert is_saas("https://api.us.hiddenlayer.ai")


def test_is_not_saas():
    """Test if a host is not our SaaS"""

    assert not is_saas("http://enterprise.deployment.com")
