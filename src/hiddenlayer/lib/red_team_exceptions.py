"""Exception classes for HiddenLayer AI Red Team SDK."""


class RedTeamSessionError(Exception):
    """Base exception for red team session errors."""


class PollTimeoutError(RedTeamSessionError):
    """Raised when polling times out."""


class WorkflowNotFoundError(RedTeamSessionError):
    """Raised when workflow is not found."""


class InvalidSessionError(RedTeamSessionError):
    """Raised when session ID is invalid."""
