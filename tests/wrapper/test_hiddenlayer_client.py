from __future__ import annotations

import warnings
from typing import Any, Dict, List, Optional
from urllib.parse import parse_qs

import httpx
import pytest

import hiddenlayer
from hiddenlayer import AsyncHiddenLayer, HiddenLayer, HiddenLayerEnvironment
from hiddenlayer._beta_endpoints import BETA_ENDPOINTS
from hiddenlayer.base_client import AsyncBaseClient, BaseClient
from hiddenlayer.client import MISSING_CREDENTIALS_MESSAGE
from hiddenlayer.core.api_error import ApiError
from hiddenlayer.lib import (
    AsyncCommunityScanner,
    AsyncEvaluationSessionsResource,
    AsyncModelScanner,
    BetaWarning,
    CommunityScanner,
    EvaluationSessionsResource,
    ModelScanner,
)
from hiddenlayer.lib._beta import AsyncBetaWarningHook, BetaWarningHook

PROD_US = "https://api.us.hiddenlayer.ai"
PROD_EU = "https://api.eu.hiddenlayer.ai"
MODEL_ID = "0b6f1c1e-7a3e-4d42-9c55-1f2e3d4c5b6a"
CREDENTIAL_VARIABLES = (
    "HIDDENLAYER_TOKEN",
    "HIDDENLAYER_CLIENT_ID",
    "HIDDENLAYER_CLIENT_SECRET",
    "HIDDENLAYER_BASE_URL",
)


class RecordingApi:
    """Answers every API request with 204, and the token endpoint with an access token."""

    def __init__(self) -> None:
        self.requests: List[httpx.Request] = []

    @property
    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self._handle)

    def _handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if request.url.path.endswith("/oauth2/token"):
            form = parse_qs(request.content.decode())
            token = f"access-token-for-{form['client_id'][0]}"
            return httpx.Response(200, json={"access_token": token, "token_type": "Bearer", "expires_in": 3600})
        return httpx.Response(204)

    @property
    def token_requests(self) -> List[Dict[str, List[str]]]:
        return [parse_qs(r.content.decode()) for r in self.requests if r.url.path.endswith("/oauth2/token")]

    @property
    def api_requests(self) -> List[httpx.Request]:
        return [r for r in self.requests if not r.url.path.endswith("/oauth2/token")]

    @property
    def authorization(self) -> Optional[str]:
        return self.api_requests[-1].headers.get("authorization")


def sync_client(api: RecordingApi, **options: Any) -> HiddenLayer:
    return HiddenLayer(httpx_client=httpx.Client(transport=api.transport), max_retries=0, **options)


def async_client(api: RecordingApi, **options: Any) -> AsyncHiddenLayer:
    return AsyncHiddenLayer(httpx_client=httpx.AsyncClient(transport=api.transport), max_retries=0, **options)


def beta_request() -> httpx.Request:
    """A request to whichever beta endpoint the API lists first, so the test survives any regeneration."""
    if not BETA_ENDPOINTS:
        pytest.skip("the API has no beta endpoints")
    method, pattern = BETA_ENDPOINTS[0]
    path = "/".join("abc123" if part.startswith("{") else part for part in pattern.split("/"))
    return httpx.Request(method, f"{PROD_US}{path}")


@pytest.fixture(autouse=True)
def clean_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    for variable in CREDENTIAL_VARIABLES:
        monkeypatch.delenv(variable, raising=False)


class TestCredentials:
    def test_a_token_argument_is_sent_as_the_bearer_token(self) -> None:
        api = RecordingApi()

        sync_client(api, token="  hl-token-from-argument\n").models.delete(MODEL_ID)

        assert api.authorization == "Bearer hl-token-from-argument"
        assert api.token_requests == []

    def test_a_token_function_is_called_for_every_request(self) -> None:
        api = RecordingApi()
        tokens = iter(["first-token", "second-token"])
        client = sync_client(api, token=lambda: next(tokens))

        client.models.delete(MODEL_ID)
        client.models.delete(MODEL_ID)

        assert [r.headers["authorization"] for r in api.api_requests] == ["Bearer first-token", "Bearer second-token"]

    def test_client_credentials_are_exchanged_once_for_an_access_token(self) -> None:
        api = RecordingApi()
        client = sync_client(api, client_id="client-from-argument", client_secret="secret-from-argument")

        client.models.delete(MODEL_ID)
        client.models.delete(MODEL_ID)

        assert api.token_requests == [
            {
                "grant_type": ["client_credentials"],
                "client_id": ["client-from-argument"],
                "client_secret": ["secret-from-argument"],
            }
        ]
        assert api.authorization == "Bearer access-token-for-client-from-argument"

    def test_the_token_variable_is_read_when_the_client_is_constructed(self, monkeypatch: pytest.MonkeyPatch) -> None:
        api = RecordingApi()
        monkeypatch.setenv("HIDDENLAYER_TOKEN", "hl-token-from-environment")

        sync_client(api).models.delete(MODEL_ID)

        assert api.authorization == "Bearer hl-token-from-environment"

    def test_the_client_credential_variables_are_read_when_the_client_is_constructed(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        api = RecordingApi()
        monkeypatch.setenv("HIDDENLAYER_CLIENT_ID", "client-from-environment")
        monkeypatch.setenv("HIDDENLAYER_CLIENT_SECRET", "secret-from-environment")

        sync_client(api).models.delete(MODEL_ID)

        assert api.token_requests[0]["client_secret"] == ["secret-from-environment"]
        assert api.authorization == "Bearer access-token-for-client-from-environment"

    @pytest.mark.parametrize(
        ("arguments", "expected"),
        [
            ({"token": "argument-token"}, "Bearer argument-token"),
            (
                {"token": "argument-token", "client_id": "argument-client", "client_secret": "argument-secret"},
                "Bearer argument-token",
            ),
            (
                {"client_id": "argument-client", "client_secret": "argument-secret"},
                "Bearer access-token-for-argument-client",
            ),
            ({"client_id": "argument-client"}, "Bearer access-token-for-argument-client"),
            ({"client_secret": "argument-secret"}, "Bearer access-token-for-environment-client"),
            ({}, "Bearer environment-token"),
            ({"token": "", "client_id": " ", "client_secret": ""}, "Bearer environment-token"),
        ],
    )
    def test_arguments_win_over_the_environment_and_a_token_over_client_credentials(
        self, monkeypatch: pytest.MonkeyPatch, arguments: Dict[str, str], expected: str
    ) -> None:
        api = RecordingApi()
        monkeypatch.setenv("HIDDENLAYER_TOKEN", "environment-token")
        monkeypatch.setenv("HIDDENLAYER_CLIENT_ID", "environment-client")
        monkeypatch.setenv("HIDDENLAYER_CLIENT_SECRET", "environment-secret")

        sync_client(api, **arguments).models.delete(MODEL_ID)

        assert api.authorization == expected

    def test_without_credentials_the_client_is_built_and_each_request_says_what_to_set(self) -> None:
        api = RecordingApi()
        client = sync_client(api)

        with pytest.raises(ApiError) as raised:
            client.models.delete(MODEL_ID)

        assert raised.value.body == MISSING_CREDENTIALS_MESSAGE
        assert api.requests == []

    @pytest.mark.parametrize("variable", ["HIDDENLAYER_CLIENT_ID", "HIDDENLAYER_CLIENT_SECRET"])
    def test_one_client_credential_alone_is_no_credential(self, monkeypatch: pytest.MonkeyPatch, variable: str) -> None:
        api = RecordingApi()
        monkeypatch.setenv(variable, "only-half")

        with pytest.raises(ApiError) as raised:
            sync_client(api).models.delete(MODEL_ID)

        assert raised.value.body == MISSING_CREDENTIALS_MESSAGE

    def test_credentials_in_the_environment_at_import_are_not_used_once_they_are_unset(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # The generated client's defaults are the variables as they were when the package was imported.
        defaults = BaseClient.__init__.__kwdefaults__
        monkeypatch.setitem(defaults, "client_id", "client-at-import")
        monkeypatch.setitem(defaults, "client_secret", "secret-at-import")
        api = RecordingApi()

        with pytest.raises(ApiError) as raised:
            sync_client(api).models.delete(MODEL_ID)

        assert raised.value.body == MISSING_CREDENTIALS_MESSAGE
        assert api.requests == []


class TestBaseUrl:
    @pytest.mark.parametrize(
        ("arguments", "expected"),
        [
            ({}, PROD_US),
            ({"environment": "prod-us"}, PROD_US),
            ({"environment": "prod-eu"}, PROD_EU),
            ({"environment": HiddenLayerEnvironment.PROD_EU}, PROD_EU),
            ({"base_url": "https://hiddenlayer.acme.example"}, "https://hiddenlayer.acme.example"),
            (
                {"base_url": "https://hiddenlayer.acme.example", "environment": "prod-eu"},
                "https://hiddenlayer.acme.example",
            ),
        ],
    )
    def test_base_url_wins_over_environment_which_defaults_to_prod_us(
        self, arguments: Dict[str, Any], expected: str
    ) -> None:
        api = RecordingApi()

        sync_client(api, token="hl-token", **arguments).models.delete(MODEL_ID)

        assert str(api.api_requests[-1].url) == f"{expected}/api/v2/models/{MODEL_ID}"

    @pytest.mark.parametrize(
        ("arguments", "expected"),
        [
            ({}, "https://hiddenlayer.from-environment.example"),
            ({"environment": "prod-eu"}, PROD_EU),
            ({"base_url": "https://hiddenlayer.acme.example"}, "https://hiddenlayer.acme.example"),
        ],
    )
    def test_the_base_url_variable_is_used_only_when_neither_argument_is_given(
        self, monkeypatch: pytest.MonkeyPatch, arguments: Dict[str, Any], expected: str
    ) -> None:
        api = RecordingApi()
        monkeypatch.setenv("HIDDENLAYER_BASE_URL", "https://hiddenlayer.from-environment.example")

        sync_client(api, token="hl-token", **arguments).models.delete(MODEL_ID)

        assert api.api_requests[-1].url.host == httpx.URL(expected).host

    def test_an_unknown_environment_name_is_refused(self) -> None:
        with pytest.raises(ValueError, match="Unknown environment: staging"):
            HiddenLayer(token="hl-token", environment="staging")  # type: ignore[arg-type]

    def test_the_token_endpoint_is_on_the_same_base_url(self) -> None:
        api = RecordingApi()

        sync_client(
            api, client_id="client-1", client_secret="secret-1", base_url="https://hiddenlayer.acme.example"
        ).models.delete(MODEL_ID)

        assert str(api.requests[0].url) == "https://hiddenlayer.acme.example/oauth2/token"


class TestHelpers:
    def test_the_client_has_the_scanners_and_red_team_sessions(self) -> None:
        client = HiddenLayer(token="hl-token")

        assert isinstance(client, BaseClient)
        assert type(client.model_scanner) is ModelScanner
        assert type(client.community_scanner) is CommunityScanner
        assert type(client.evaluation_sessions) is EvaluationSessionsResource
        assert client.model_scanner is client.model_scanner
        assert client.evaluation_sessions.red_team is client.evaluation_sessions.red_team

    def test_the_async_client_has_the_async_scanners_and_red_team_sessions(self) -> None:
        client = AsyncHiddenLayer(token="hl-token")

        assert isinstance(client, AsyncBaseClient)
        assert type(client.model_scanner) is AsyncModelScanner
        assert type(client.community_scanner) is AsyncCommunityScanner
        assert type(client.evaluation_sessions) is AsyncEvaluationSessionsResource
        assert client.community_scanner is client.community_scanner

    def test_the_package_exports_the_clients_and_the_names_3x_exported_from_lib(self) -> None:
        assert hiddenlayer.HiddenLayer is HiddenLayer
        assert hiddenlayer.AsyncHiddenLayer is AsyncHiddenLayer
        assert hiddenlayer.ModelScanner is ModelScanner
        assert hiddenlayer.AsyncModelScanner is AsyncModelScanner
        assert hiddenlayer.CommunityScanner is CommunityScanner
        assert hiddenlayer.AsyncCommunityScanner is AsyncCommunityScanner
        assert hiddenlayer.BetaWarning is BetaWarning
        assert callable(hiddenlayer.warn_beta)


class TestBetaWarnings:
    def test_the_first_call_to_a_beta_endpoint_warns_and_later_calls_do_not(self) -> None:
        api = RecordingApi()
        client = sync_client(api, token="hl-token")
        request = beta_request()
        low_level = client._client_wrapper.httpx_client

        with pytest.warns(BetaWarning) as caught:
            low_level.request(request.url.path, method=request.method)
        with warnings.catch_warnings(record=True) as later:
            warnings.simplefilter("always")
            low_level.request(request.url.path, method=request.method)

        assert [str(w.message).split(":")[0] for w in caught] == [f"[BETA] {' '.join(BETA_ENDPOINTS[0])}"]
        assert [w for w in later if issubclass(w.category, BetaWarning)] == []
        assert len(api.api_requests) == 2

    def test_clients_that_share_an_httpx_client_share_one_hook_for_each_base_url(self) -> None:
        http_client = httpx.Client(transport=RecordingApi().transport)

        for _ in range(3):
            HiddenLayer(token="hl-token", httpx_client=http_client)
        HiddenLayer(token="hl-token", environment="prod-eu", httpx_client=http_client)

        hooks = http_client.event_hooks["request"]
        assert all(type(hook) is BetaWarningHook for hook in hooks)
        assert [hook.base_url for hook in hooks if isinstance(hook, BetaWarningHook)] == [PROD_US, PROD_EU]

    async def test_the_async_client_warns_on_the_first_call_to_a_beta_endpoint(self) -> None:
        api = RecordingApi()
        client = async_client(api, token="hl-token")
        request = beta_request()
        low_level = client._client_wrapper.httpx_client

        with pytest.warns(BetaWarning) as caught:
            await low_level.request(request.url.path, method=request.method)
            await low_level.request(request.url.path, method=request.method)

        assert len(caught) == 1
        assert [type(hook) for hook in client._client_wrapper.httpx_client.httpx_client.event_hooks["request"]] == [
            AsyncBetaWarningHook
        ]


class TestAsyncCredentials:
    async def test_a_token_argument_is_sent_as_the_bearer_token(self) -> None:
        api = RecordingApi()

        await async_client(api, token="hl-token-from-argument").models.delete(MODEL_ID)

        assert api.authorization == "Bearer hl-token-from-argument"

    async def test_an_async_token_function_is_awaited_and_wins_over_everything_else(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        api = RecordingApi()
        monkeypatch.setenv("HIDDENLAYER_TOKEN", "environment-token")

        async def fetch_token() -> str:
            return "token-from-async-function"

        client = async_client(api, async_token=fetch_token, token="argument-token", client_id="argument-client")
        await client.models.delete(MODEL_ID)

        assert api.authorization == "Bearer token-from-async-function"

    async def test_client_credentials_are_exchanged_once_for_an_access_token(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        api = RecordingApi()
        monkeypatch.setenv("HIDDENLAYER_CLIENT_ID", "client-from-environment")
        monkeypatch.setenv("HIDDENLAYER_CLIENT_SECRET", "secret-from-environment")
        client = async_client(api, environment="prod-eu")

        await client.models.delete(MODEL_ID)
        await client.models.delete(MODEL_ID)

        assert len(api.token_requests) == 1
        assert str(api.requests[0].url) == f"{PROD_EU}/oauth2/token"
        assert api.authorization == "Bearer access-token-for-client-from-environment"

    async def test_without_credentials_each_request_says_what_to_set(self) -> None:
        api = RecordingApi()
        client = async_client(api)

        with pytest.raises(ApiError) as raised:
            await client.models.delete(MODEL_ID)

        assert raised.value.body == MISSING_CREDENTIALS_MESSAGE
        assert api.requests == []

    async def test_credentials_in_the_environment_at_import_are_not_used_once_they_are_unset(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        defaults = AsyncBaseClient.__init__.__kwdefaults__
        monkeypatch.setitem(defaults, "client_id", "client-at-import")
        monkeypatch.setitem(defaults, "client_secret", "secret-at-import")
        api = RecordingApi()

        with pytest.raises(ApiError):
            await async_client(api).models.delete(MODEL_ID)

        assert api.requests == []
