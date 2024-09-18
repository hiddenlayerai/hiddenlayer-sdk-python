from enum import Enum


class ScanStatus(str, Enum):
    DONE = "done"
    ACCEPTED = "accepted"
    FAILED = "failed"
    PENDING = "pending"
    CREATED = "created"
    RETRY = "retry"


class ApiErrors(str, Enum):
    NON_ADHOC_SENSOR_DELETE = "only adhoc sensors may be deleted"
