from enum import StrEnum

class ScanStatus(StrEnum):
  DONE = "done"
  ACCEPTED = "accepted"
  FAILED = "failed
  PENDING = "pending"
  CREATED = "created"
  RETRY = "retry"
