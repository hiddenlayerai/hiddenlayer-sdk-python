"""Warnings for calls to beta API endpoints, which can change without a major release."""

from __future__ import annotations

import warnings
from typing import List, Optional, Sequence, Set, Tuple, Union

import httpx
from .._beta_endpoints import BETA_ENDPOINTS

# Each endpoint's HTTP method and its path, with `{param}` for each path parameter.
Endpoints = Sequence[Tuple[str, str]]


class BetaWarning(UserWarning):
    """Warning emitted when a beta API endpoint is called."""


def warn_beta(qualified_name: str, *, stacklevel: int = 3) -> None:
    """Emits a BetaWarning for a beta endpoint.

    Args:
        qualified_name: The endpoint, e.g. "GET /access/v2/api-keys".
        stacklevel: How many frames to skip when reporting the warning's location.
    """
    warnings.warn(
        f"[BETA] {qualified_name}: This endpoint is not GA or Production ready "
        "and is subject to changes at any time. Breaking changes may occur.",
        BetaWarning,
        stacklevel=stacklevel,
    )


def _segments(path: str) -> List[str]:
    return [segment for segment in path.split("?", 1)[0].split("/") if segment]


def _matches(pattern: List[str], segments: List[str]) -> bool:
    return len(pattern) == len(segments) and all(
        (part.startswith("{") and part.endswith("}")) or part == segment for part, segment in zip(pattern, segments)
    )


def find_beta_endpoint(
    url: str, method: Optional[str] = None, *, endpoints: Endpoints = BETA_ENDPOINTS
) -> Optional[str]:
    """Returns the beta endpoint a request is to, as "METHOD /path/{param}", or None.

    Args:
        url: The request's path below the API's base URL. A query string is ignored.
        method: The HTTP method. Any method matches when it is omitted.
        endpoints: The beta endpoints. Defaults to the API's, as of the SDK's generation.
    """
    segments = _segments(url)
    for endpoint_method, pattern in endpoints:
        if method is not None and endpoint_method != method.upper():
            continue
        if _matches(_segments(pattern), segments):
            return f"{endpoint_method} {pattern}"
    return None


def check_beta_endpoint(url: str, method: Optional[str] = None) -> None:
    """Emits a BetaWarning when a request is to a beta endpoint.

    Args:
        url: The request's path below the API's base URL, e.g. "/access/v2/api-keys".
        method: The HTTP method. Any method matches when it is omitted.
    """
    endpoint = find_beta_endpoint(url, method)
    if endpoint is not None:
        warn_beta(endpoint)


class _BetaEndpointWatch:
    """Warns the first time each beta endpoint under a base URL is requested.

    Requests to any other origin than the API's, such as a presigned upload URL, are not checked.
    """

    def __init__(self, base_url: str, endpoints: Endpoints = BETA_ENDPOINTS) -> None:
        self.base_url = base_url
        self._endpoints = endpoints
        self._url = httpx.URL(base_url)
        self._base_path = self._raw_path(self._url).rstrip("/")
        self._warned: Set[str] = set()

    def check(self, request: httpx.Request) -> None:
        path = self._api_path(request.url)
        if path is None:
            return
        endpoint = find_beta_endpoint(path, request.method, endpoints=self._endpoints)
        if endpoint is None or endpoint in self._warned:
            return
        warn_beta(endpoint, stacklevel=4)
        # Recorded only once the warning is out: under a filter that raises it, every call keeps raising.
        self._warned.add(endpoint)

    @staticmethod
    def _raw_path(url: httpx.URL) -> str:
        # Undecoded, so an encoded slash in a path parameter stays inside its segment.
        return url.raw_path.decode("ascii").split("?", 1)[0]

    def _api_path(self, url: httpx.URL) -> Optional[str]:
        base = self._url
        if (url.scheme, url.host, url.port) != (base.scheme, base.host, base.port):
            return None
        path = self._raw_path(url)
        if self._base_path and not path.startswith(f"{self._base_path}/"):
            return None
        return path[len(self._base_path) :]


class BetaWarningHook(_BetaEndpointWatch):
    """An httpx.Client request hook."""

    def __call__(self, request: httpx.Request) -> None:
        self.check(request)


class AsyncBetaWarningHook(_BetaEndpointWatch):
    """An httpx.AsyncClient request hook, which that client awaits."""

    async def __call__(self, request: httpx.Request) -> None:
        self.check(request)


def add_beta_warnings(
    httpx_client: Union[httpx.Client, httpx.AsyncClient], base_url: str, endpoints: Endpoints = BETA_ENDPOINTS
) -> None:
    """Has an httpx client warn the first time each beta endpoint under base_url is requested through it.

    Adding the same base URL to the same httpx client again changes nothing, so clients that share an
    httpx client share one hook.
    """
    hooks = httpx_client.event_hooks["request"]
    if any(isinstance(hook, _BetaEndpointWatch) and hook.base_url == base_url for hook in hooks):
        return
    if isinstance(httpx_client, httpx.AsyncClient):
        hooks.append(AsyncBetaWarningHook(base_url, endpoints))
    else:
        hooks.append(BetaWarningHook(base_url, endpoints))
