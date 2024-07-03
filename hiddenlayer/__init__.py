from typing import Optional

import requests
from requests.auth import HTTPBasicAuth

from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.configuration import Configuration
from hiddenlayer.sdk.services.aidr_predictive import AIDRPredictive
from hiddenlayer.sdk.services.model import ModelAPI
from hiddenlayer.sdk.services.model_scan import ModelScanAPI
from hiddenlayer.sdk.utils import is_saas
from hiddenlayer.sdk.version import VERSION

__version__ = VERSION


class HiddenlayerServiceAuthError(Exception):
    pass


class HiddenlayerUnsupportedPlatformError(Exception):
    pass


class HiddenlayerServiceClient:
    """
    The Hiddenlayer Service Client is a client for the Hiddenlayer services REST API.
    """

    def __init__(
        self,
        *,
        api_id: Optional[str] = None,
        api_key: Optional[str] = None,
        host: str = "https://api.us.hiddenlayer.ai",
    ):
        self.is_saas = is_saas(host)

        if self.is_saas:
            if not api_id:
                raise EnvironmentError(
                    "`api_id` cannot be None when using the SaaS version of HiddenLayer."
                )

            if not api_key:
                raise EnvironmentError(
                    "`api_key` cannot be None when using the SaaS version of HiddenLayer."
                )

            jwt_token = self._get_jwt(api_id=api_id, api_key=api_key)
            self._config = Configuration(host=host, access_token=jwt_token)

        else:
            self._config = Configuration(host=host)

        self._api_client = ApiClient(configuration=self._config)
        self._aidr_predictive = AIDRPredictive(self._api_client)
        self._model = ModelAPI(self._api_client)
        self._model_scan = ModelScanAPI(self._api_client)

    def _get_jwt(self, *, api_id: str, api_key: str) -> str:
        "Get the JWT token to auth to the Hiddenlayer API."

        token_url = (
            "https://auth.hiddenlayer.ai/oauth2/token?grant_type=client_credentials"
        )

        resp = requests.post(token_url, auth=HTTPBasicAuth(api_id, api_key))

        if not resp.ok:
            raise HiddenlayerServiceAuthError(
                f"Unable to get authentication credentials for the HiddenLayer API: {resp.status_code}: {resp.text}"
            )

        if "access_token" not in resp.json():
            raise HiddenlayerServiceAuthError(
                f"Unable to get authentication credentials for the HiddenLayer API - invalid response: {resp.json()}"
            )

        return resp.json()["access_token"]

    @property
    def config(self) -> Configuration:
        return self._config

    @property
    def api_client(self) -> ApiClient:
        return self._api_client

    @property
    def model_scanner(self) -> ModelScanAPI:
        return self._model_scan

    @property
    def aidr_predictive(self) -> AIDRPredictive:
        # If the platform is not SaaS, it's not supported
        if not self.is_saas:
            raise HiddenlayerUnsupportedPlatformError(
                "AIDR for Predictive Models is currently only supported with the SaaS version of the platform."
            )
        return self._aidr_predictive

    @property
    def model(self) -> ModelAPI:
        if not self.is_saas:
            raise HiddenlayerUnsupportedPlatformError(
                "Model management is currently only supported with the SaaS version of the platform."
            )
        return self._model
