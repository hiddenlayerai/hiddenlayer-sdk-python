import pytest

from hiddenlayer import HiddenlayerServiceClient, HiddenlayerUnsupportedPlatformError


def test_fail_api_id_missing():
    """Test accessing SaaS without api id"""

    with pytest.raises(EnvironmentError):
        HiddenlayerServiceClient()


def test_fail_api_key_missing():
    """Test accessing SaaS without api key"""

    with pytest.raises(EnvironmentError):
        HiddenlayerServiceClient(api_id="test")


def test_fail_access_aidr_predictive():
    """Test failing accessing to AIDR Predictive for non SaaS deployments."""

    hl_client = HiddenlayerServiceClient(host="http://localhost:8000")

    with pytest.raises(HiddenlayerUnsupportedPlatformError):
        hl_client.aidr_predictive.submit_vectors


def test_fail_access_model():
    """Test failing accessing model management for non SaaS deployments."""

    hl_client = HiddenlayerServiceClient(host="http://localhost:8000")

    with pytest.raises(HiddenlayerUnsupportedPlatformError):
        hl_client.model.get
