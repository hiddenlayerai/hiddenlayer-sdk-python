"""Runtime beta warning utility.

Emits a warning when a beta endpoint is called, so SDK consumers know
the method is not yet GA.
"""

from __future__ import annotations

import warnings


class BetaWarning(UserWarning):
    """Warning emitted when a beta API endpoint is called."""


def warn_beta(qualified_name: str, *, stacklevel: int = 3) -> None:
    """Emit a warning that a beta endpoint was called.

    Args:
        qualified_name: Fully qualified method name, e.g. "InteractionsResource.analyze"
        stacklevel: How many frames to skip when reporting the warning location.
    """
    warnings.warn(
        f"[BETA] {qualified_name}: This endpoint is not GA or Production ready "
        "and is subject to changes at any time. Breaking changes may occur.",
        BetaWarning,
        stacklevel=stacklevel,
    )


def check_beta_endpoint(url: str) -> None:
    """Check whether *url* is a beta endpoint and emit a warning if so.

    Args:
        url: The URL path for the request (e.g. "/detection/v2/request-evaluations").
    """
    from ._beta_endpoints import BETA_ENDPOINTS

    qualified_name = BETA_ENDPOINTS.get(url)
    if qualified_name is not None:
        # Called from _prepare_options, which is deeper in the stack than
        # a direct warn_beta call from a resource method.  The higher
        # stacklevel won't point at user code, but the message itself
        # identifies the method.
        warn_beta(qualified_name, stacklevel=4)
