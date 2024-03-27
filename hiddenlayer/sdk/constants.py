from enum import Enum


class ScanStatus(str, Enum):
    DONE = "done"
    ACCEPTED = "accepted"
    FAILED = "failed"
    PENDING = "pending"
    CREATED = "created"
    RETRY = "retry"
