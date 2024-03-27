import requests
from requests.auth import HTTPBasicAuth

from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.configuration import Configuration
from hiddenlayer.sdk.services.mldr import MLDRAPI
from hiddenlayer.sdk.services.model import ModelAPI
from hiddenlayer.sdk.services.model_scan import ModelScanAPI


class HiddenlayerServiceAuthError(Exception):
    pass


class HiddenlayerServiceClient:
    """
    The Hiddenlayer Service Client is a client for the Hiddenlayer services REST API.
    """

    def __init__(self, *, host: str, api_id: str, api_key: str):
        jwt_token = self._get_jwt(api_id=api_id, api_key=api_key)

        self._config = Configuration(host=host, access_token=jwt_token)
        self._api_client = ApiClient(configuration=self._config)
        self._model_scan = ModelScanAPI(self._api_client)
        self._mldr = MLDRAPI(self._api_client)
        self._model = ModelAPI(self._api_client)

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
    def mldr(self) -> MLDRAPI:
        return self._mldr

    @property
    def model(self) -> ModelAPI:
        return self._model
