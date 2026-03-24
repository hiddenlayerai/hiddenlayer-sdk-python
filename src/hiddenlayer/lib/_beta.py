"""Runtime beta warning utility.

Emits a warning when a beta endpoint is called, so SDK consumers know
the method is not yet GA.
"""

from __future__ import annotations

import warnings


class BetaWarning(UserWarning):
    """Warning emitted when a beta API endpoint is called."""


def warn_beta(qualified_name: str) -> None:
    """Emit a warning that a beta endpoint was called.

    Args:
        qualified_name: Fully qualified method name, e.g. "InteractionsResource.analyze"
    """
    warnings.warn(
        f"[BETA] {qualified_name}: This endpoint is not GA or Production ready "
        "and is subject to changes at any time. Breaking changes may occur.",
        BetaWarning,
        stacklevel=3,
    )
