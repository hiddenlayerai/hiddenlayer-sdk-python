"""The HiddenLayer clients: the generated clients plus credentials and the base URL from the environment,
the model and community scanners, red team sessions and beta warnings."""

import os
import typing
from functools import cached_property

import httpx
from .base_client import AsyncBaseClient, BaseClient
from .core.api_error import ApiError
from .core.logging import LogConfig, Logger
from .environment import HiddenLayerEnvironment
from .lib._beta import add_beta_warnings
from .lib.community_scan import AsyncCommunityScanner, CommunityScanner
from .lib.evaluation_sessions import AsyncEvaluationSessionsResource, EvaluationSessionsResource
from .lib.model_scan import AsyncModelScanner, ModelScanner

EnvironmentName = typing.Literal["prod-us", "prod-eu"]

MISSING_CREDENTIALS_MESSAGE = (
    "No HiddenLayer credentials: pass token, or client_id and client_secret, to the client, or set "
    "HIDDENLAYER_TOKEN, or HIDDENLAYER_CLIENT_ID and HIDDENLAYER_CLIENT_SECRET."
)

_ENVIRONMENTS: typing.Dict[str, HiddenLayerEnvironment] = {
    "prod-us": HiddenLayerEnvironment.PROD_US,
    "prod-eu": HiddenLayerEnvironment.PROD_EU,
}


def _non_blank(value: typing.Optional[str]) -> typing.Optional[str]:
    return (value.strip() or None) if value is not None else None


def _read_env(name: str) -> typing.Optional[str]:
    return _non_blank(os.environ.get(name))


def _missing_credentials() -> str:
    raise ApiError(body=MISSING_CREDENTIALS_MESSAGE)


def _credentials(
    token: typing.Optional[typing.Union[str, typing.Callable[[], str]]],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
) -> typing.Dict[str, typing.Any]:
    """The base client's credential arguments.

    Arguments win over the environment: token, then client_id and client_secret, then HIDDENLAYER_TOKEN,
    then HIDDENLAYER_CLIENT_ID and HIDDENLAYER_CLIENT_SECRET. A blank string counts as not given. Both
    client credentials are always passed, so the base client's own defaults, the environment as it was
    when the package was imported, are never used.
    """
    passed_token = _non_blank(token) if isinstance(token, str) else token
    if passed_token is not None:
        return {"token": passed_token, "client_id": None, "client_secret": None}

    passed_id, passed_secret = _non_blank(client_id), _non_blank(client_secret)
    resolved_id = passed_id or _read_env("HIDDENLAYER_CLIENT_ID")
    resolved_secret = passed_secret or _read_env("HIDDENLAYER_CLIENT_SECRET")
    client_credentials = {"client_id": resolved_id, "client_secret": resolved_secret}
    has_client_credentials = resolved_id is not None and resolved_secret is not None
    if has_client_credentials and (passed_id is not None or passed_secret is not None):
        return client_credentials

    env_token = _read_env("HIDDENLAYER_TOKEN")
    if env_token is not None:
        return {"token": env_token, "client_id": None, "client_secret": None}
    if has_client_credentials:
        return client_credentials
    # Raised by each request rather than here, so a client can be constructed before its credentials are set.
    return {"token": _missing_credentials, "client_id": None, "client_secret": None}


def _environment(
    environment: typing.Optional[typing.Union[HiddenLayerEnvironment, EnvironmentName]],
) -> HiddenLayerEnvironment:
    if environment is None:
        return HiddenLayerEnvironment.PROD_US
    if isinstance(environment, HiddenLayerEnvironment):
        return environment
    if environment not in _ENVIRONMENTS:
        raise ValueError(f"Unknown environment: {environment}")
    return _ENVIRONMENTS[environment]


def _base_url(
    base_url: typing.Optional[str],
    environment: typing.Optional[typing.Union[HiddenLayerEnvironment, EnvironmentName]],
) -> typing.Optional[str]:
    if base_url is not None or environment is not None:
        return base_url
    return _read_env("HIDDENLAYER_BASE_URL")


class HiddenLayer(BaseClient):
    """The HiddenLayer API client.

    Args:
        token: A bearer token, or a function that returns one, called for every request. Defaults to
            HIDDENLAYER_TOKEN.
        client_id: Exchanged with client_secret for an access token, which is renewed before it expires.
            Defaults to HIDDENLAYER_CLIENT_ID.
        client_secret: Defaults to HIDDENLAYER_CLIENT_SECRET.
        environment: A region, as "prod-us", "prod-eu" or a HiddenLayerEnvironment. Defaults to prod-us.
        base_url: A URL that overrides environment. Defaults to HIDDENLAYER_BASE_URL when environment
            isn't given either.
        headers: Headers sent with every request.
        timeout: Seconds before a request times out. Defaults to 60, or to httpx_client's own when one
            is given.
        max_retries: Retries of a failed request. Defaults to 2.
        follow_redirects: Whether the default httpx client follows redirects.
        httpx_client: The httpx client to send requests with. The client adds a request hook to it,
            for beta warnings.

    A token or both client credentials given as arguments are used before any from the environment,
    and a token before client credentials. With no credentials at all the client can still be
    constructed, and each request raises an ApiError that names what to set.
    """

    def __init__(
        self,
        *,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        environment: typing.Optional[typing.Union[HiddenLayerEnvironment, EnvironmentName]] = None,
        base_url: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ) -> None:
        super().__init__(
            base_url=_base_url(base_url, environment),
            environment=_environment(environment),
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
            **_credentials(token, client_id, client_secret),
        )
        add_beta_warnings(self._client_wrapper.httpx_client.httpx_client, self._client_wrapper.get_base_url())

    @cached_property
    def model_scanner(self) -> ModelScanner:
        """Scans local files and folders, and models in S3, Azure Blob Storage and Hugging Face."""
        return ModelScanner(self)

    @cached_property
    def community_scanner(self) -> CommunityScanner:
        """Scans a model at a remote location the scanner fetches itself."""
        return CommunityScanner(self)

    @cached_property
    def evaluation_sessions(self) -> EvaluationSessionsResource:
        """Runs red team sessions against a target you call yourself."""
        return EvaluationSessionsResource(self)


class AsyncHiddenLayer(AsyncBaseClient):
    """The asynchronous HiddenLayer API client.

    Takes the arguments of HiddenLayer, with an httpx.AsyncClient as httpx_client, and:

    Args:
        async_token: An async function that returns a bearer token, awaited for every request. Used
            before any other credential.
    """

    def __init__(
        self,
        *,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        environment: typing.Optional[typing.Union[HiddenLayerEnvironment, EnvironmentName]] = None,
        base_url: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ) -> None:
        credentials: typing.Dict[str, typing.Any] = (
            _credentials(token, client_id, client_secret)
            if async_token is None
            else {"async_token": async_token, "client_id": None, "client_secret": None}
        )
        super().__init__(
            base_url=_base_url(base_url, environment),
            environment=_environment(environment),
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
            **credentials,
        )
        add_beta_warnings(self._client_wrapper.httpx_client.httpx_client, self._client_wrapper.get_base_url())

    @cached_property
    def model_scanner(self) -> AsyncModelScanner:
        """Scans local files and folders, and models in S3, Azure Blob Storage and Hugging Face."""
        return AsyncModelScanner(self)

    @cached_property
    def community_scanner(self) -> AsyncCommunityScanner:
        """Scans a model at a remote location the scanner fetches itself."""
        return AsyncCommunityScanner(self)

    @cached_property
    def evaluation_sessions(self) -> AsyncEvaluationSessionsResource:
        """Runs red team sessions against a target you call yourself."""
        return AsyncEvaluationSessionsResource(self)
