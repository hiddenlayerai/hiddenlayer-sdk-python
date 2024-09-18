class HiddenlayerConflictError(Exception):
    """Generic error class for API errors from a 409 error code."""

    pass


class ModelDoesNotExistError(Exception):
    pass


class IncompatibleModelError(Exception):
    pass
