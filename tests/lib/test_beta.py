from __future__ import annotations

import warnings
from typing import List, Optional

import httpx
import pytest

from hiddenlayer.lib._beta import (
    AsyncBetaWarningHook,
    BetaWarning,
    BetaWarningHook,
    add_beta_warnings,
    find_beta_endpoint,
    warn_beta,
)

# The API's own list changes with every generation, so these tests bring their own.
ENDPOINTS = (
    ("GET", "/access/v2/api-keys"),
    ("POST", "/access/v2/api-keys"),
    ("DELETE", "/access/v2/api-keys/{id}/secrets/{secret_id}"),
    ("GET", "/evaluations/v2/red-team/{workflow_id}/sessions"),
)
API_URL = "https://api.hiddenlayer.test"


def beta_messages(caught: List[warnings.WarningMessage]) -> List[str]:
    return [str(warning.message) for warning in caught if issubclass(warning.category, BetaWarning)]


def test_warn_beta_emits_a_beta_warning_naming_the_endpoint() -> None:
    with pytest.warns(BetaWarning) as caught:
        warn_beta("GET /access/v2/api-keys")

    assert beta_messages(list(caught)) == [
        "[BETA] GET /access/v2/api-keys: This endpoint is not GA or Production ready "
        "and is subject to changes at any time. Breaking changes may occur."
    ]
    assert issubclass(BetaWarning, UserWarning)


@pytest.mark.parametrize(
    ("url", "method", "expected"),
    [
        ("/access/v2/api-keys", "GET", "GET /access/v2/api-keys"),
        ("/access/v2/api-keys", "post", "POST /access/v2/api-keys"),
        ("/access/v2/api-keys", None, "GET /access/v2/api-keys"),
        ("access/v2/api-keys/", "GET", "GET /access/v2/api-keys"),
        ("/access/v2/api-keys?limit=10&name=ci/cd", "GET", "GET /access/v2/api-keys"),
        (
            "/access/v2/api-keys/key-41/secrets/secret-7",
            "DELETE",
            "DELETE /access/v2/api-keys/{id}/secrets/{secret_id}",
        ),
        (
            "/evaluations/v2/red-team/0c1e/sessions",
            "GET",
            "GET /evaluations/v2/red-team/{workflow_id}/sessions",
        ),
        ("/access/v2/api-keys", "DELETE", None),
        ("/access/v2/api-keys/key-41", "GET", None),
        ("/access/v2/api-keys/key-41/secrets", "DELETE", None),
        ("/evaluations/v2/red-team/0c1e/results", "GET", None),
        ("/scan/v3/results", "GET", None),
        ("", "GET", None),
    ],
)
def test_find_beta_endpoint_matches_the_method_and_each_path_segment(
    url: str, method: Optional[str], expected: Optional[str]
) -> None:
    assert find_beta_endpoint(url, method, endpoints=ENDPOINTS) == expected


@pytest.mark.parametrize(
    ("base_url", "request_url"),
    [
        (API_URL, f"{API_URL}/access/v2/api-keys"),
        (f"{API_URL}/", f"{API_URL}/access/v2/api-keys?limit=10"),
        (f"{API_URL}/tenants/acme", f"{API_URL}/tenants/acme/access/v2/api-keys"),
        ("http://localhost:8080", "http://localhost:8080/access/v2/api-keys"),
    ],
)
def test_hook_warns_for_a_beta_endpoint_under_the_base_url(base_url: str, request_url: str) -> None:
    hook = BetaWarningHook(base_url, ENDPOINTS)

    with pytest.warns(BetaWarning, match=r"\[BETA\] GET /access/v2/api-keys:"):
        hook(httpx.Request("GET", request_url))


@pytest.mark.parametrize(
    "request_url",
    [
        f"{API_URL}/scan/v3/results",
        "https://uploads.hiddenlayer.test/tenants/acme/access/v2/api-keys",
        "http://api.hiddenlayer.test/tenants/acme/access/v2/api-keys",
        f"{API_URL}:8443/tenants/acme/access/v2/api-keys",
        f"{API_URL}/access/v2/api-keys",
        f"{API_URL}/tenants/acme-eu/access/v2/api-keys",
    ],
)
def test_hook_ignores_other_endpoints_origins_and_base_paths(request_url: str) -> None:
    hook = BetaWarningHook(f"{API_URL}/tenants/acme", ENDPOINTS)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        hook(httpx.Request("GET", request_url))

    assert beta_messages(caught) == []


def test_hook_keeps_an_encoded_slash_inside_its_path_parameter() -> None:
    hook = BetaWarningHook(API_URL, ENDPOINTS)

    with pytest.warns(BetaWarning, match=r"DELETE /access/v2/api-keys/\{id\}/secrets/\{secret_id\}"):
        hook(httpx.Request("DELETE", f"{API_URL}/access/v2/api-keys/team%2Fci/secrets/secret-7"))


def test_hook_warns_once_for_each_endpoint() -> None:
    hook = BetaWarningHook(API_URL, ENDPOINTS)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        hook(httpx.Request("GET", f"{API_URL}/access/v2/api-keys"))
        hook(httpx.Request("GET", f"{API_URL}/access/v2/api-keys?limit=10"))
        hook(httpx.Request("POST", f"{API_URL}/access/v2/api-keys"))
        hook(httpx.Request("GET", f"{API_URL}/evaluations/v2/red-team/0c1e/sessions"))
        hook(httpx.Request("GET", f"{API_URL}/evaluations/v2/red-team/77aa/sessions"))

    assert [message.split(":")[0] for message in beta_messages(caught)] == [
        "[BETA] GET /access/v2/api-keys",
        "[BETA] POST /access/v2/api-keys",
        "[BETA] GET /evaluations/v2/red-team/{workflow_id}/sessions",
    ]


def test_hook_keeps_raising_when_beta_warnings_are_errors() -> None:
    hook = BetaWarningHook(API_URL, ENDPOINTS)

    with warnings.catch_warnings():
        warnings.simplefilter("error", BetaWarning)
        for _ in range(2):
            with pytest.raises(BetaWarning):
                hook(httpx.Request("GET", f"{API_URL}/access/v2/api-keys"))


async def test_async_hook_warns_once_for_each_endpoint() -> None:
    hook = AsyncBetaWarningHook(API_URL, ENDPOINTS)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        await hook(httpx.Request("GET", f"{API_URL}/access/v2/api-keys"))
        await hook(httpx.Request("GET", f"{API_URL}/access/v2/api-keys"))

    assert len(beta_messages(caught)) == 1


def test_add_beta_warnings_adds_one_hook_for_each_base_url() -> None:
    http_client = httpx.Client()

    add_beta_warnings(http_client, API_URL, ENDPOINTS)
    add_beta_warnings(http_client, API_URL, ENDPOINTS)
    add_beta_warnings(http_client, "https://api.eu.hiddenlayer.test", ENDPOINTS)

    hooks = http_client.event_hooks["request"]
    assert all(type(hook) is BetaWarningHook for hook in hooks)
    assert [hook.base_url for hook in hooks if isinstance(hook, BetaWarningHook)] == [
        API_URL,
        "https://api.eu.hiddenlayer.test",
    ]


def test_add_beta_warnings_gives_an_async_client_a_hook_it_can_await() -> None:
    http_client = httpx.AsyncClient()

    add_beta_warnings(http_client, API_URL, ENDPOINTS)

    assert [type(hook) for hook in http_client.event_hooks["request"]] == [AsyncBetaWarningHook]
