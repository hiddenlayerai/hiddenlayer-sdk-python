from enum import Enum


class CommunityScanSource(str, Enum):
    LOCAL = "LOCAL"
    AWS_PRESIGNED = "AWS_PRESIGNED"
    AWS_IAM_ROLE = "AWS_IAM_ROLE"
    AZURE_BLOB_SAS = "AZURE_BLOB_SAS"
    AZURE_BLOB_AD = "AZURE_BLOB_AD"
    GOOGLE_SIGNED = "GOOGLE_SIGNED"
    GOOGLE_OAUTH = "GOOGLE_OAUTH"
    HUGGING_FACE = "HUGGING_FACE"


class ScanStatus(str, Enum):
    DONE = "done"
    ACCEPTED = "accepted"
    FAILED = "failed"
    PENDING = "pending"
    CREATED = "created"
    RETRY = "retry"


class ApiErrors(str, Enum):
    NON_ADHOC_SENSOR_DELETE = "only adhoc sensors may be deleted"
    SENSOR_EXISTS = "already exists"
