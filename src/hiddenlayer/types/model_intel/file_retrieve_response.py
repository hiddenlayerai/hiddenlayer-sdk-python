# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "FileRetrieveResponse",
    "FileInstance",
    "FileInstanceInstance",
    "FileInstanceLicense",
    "FileInstanceRepoOwner",
    "FileInstanceRepoRevision",
    "FileInstanceRepository",
    "FileInstanceUsePolicy",
]


class FileInstanceInstance(BaseModel):
    created_at: datetime
    """Timestamp when the file instance was created"""

    path: str
    """File path within the repository"""

    revision_id: str
    """UUID of the repository revision"""

    sha256: str
    """SHA256 hash of the file"""

    source: str
    """Source of the file instance"""

    tags: List[str]
    """Tags associated with the file instance"""

    updated_at: datetime
    """Timestamp when the file instance was last updated"""


class FileInstanceLicense(BaseModel):
    id: str
    """UUID of the license"""

    created_at: datetime
    """Timestamp when the license was created"""

    name: str
    """Name of the license"""

    sha256: str
    """SHA256 hash of the license text"""

    updated_at: datetime
    """Timestamp when the license was last updated"""

    url: str
    """URL of the license"""

    version: str
    """Version of the license"""

    description: Optional[str] = None
    """Description of the license"""

    spdx_id: Optional[str] = None
    """SPDX identifier for the license"""


class FileInstanceRepoOwner(BaseModel):
    id: str
    """UUID of the contributor"""

    country: str
    """Country of the contributor"""

    created_at: datetime
    """Timestamp when the contributor was created"""

    handle: str
    """Handle or username of the contributor"""

    homepage_url: str
    """Homepage URL of the contributor"""

    kind: str
    """Type of contributor"""

    metadata: Dict[str, object]
    """Additional metadata for the contributor"""

    source: str
    """Source platform of the contributor"""

    tags: List[str]
    """Tags associated with the contributor"""

    trust_level: str
    """Trust level of the contributor"""

    updated_at: datetime
    """Timestamp when the contributor was last updated"""

    display_name: Optional[str] = None
    """Display name of the contributor"""


class FileInstanceRepoRevision(BaseModel):
    id: str
    """UUID of the repository revision"""

    commit_hash: str
    """Git commit hash"""

    created_at: datetime
    """Timestamp when the revision was created"""

    fetched_at: datetime
    """Timestamp when the revision was fetched"""

    metadata: Dict[str, object]
    """Additional metadata for the revision"""

    repository_id: str
    """UUID of the repository"""

    updated_at: datetime
    """Timestamp when the revision was last updated"""


class FileInstanceRepository(BaseModel):
    id: str
    """UUID of the repository"""

    architectures: List[str]
    """Supported architectures"""

    created_at: datetime
    """Timestamp when the repository was created"""

    metadata: Dict[str, object]
    """Additional metadata for the repository"""

    modalities: List[str]
    """Supported modalities"""

    owner_id: str
    """UUID of the repository owner"""

    tags: List[str]
    """Tags associated with the repository"""

    updated_at: datetime
    """Timestamp when the repository was last updated"""

    url: str
    """URL of the repository"""

    description: Optional[str] = None
    """Description of the repository"""

    name: Optional[str] = None
    """Name of the repository"""


class FileInstanceUsePolicy(BaseModel):
    id: str
    """UUID of the use policy"""

    created_at: datetime
    """Timestamp when the use policy was created"""

    sha256: str
    """SHA256 hash of the policy text"""

    title: str
    """Title of the use policy"""

    updated_at: datetime
    """Timestamp when the use policy was last updated"""

    url: str
    """URL of the use policy"""

    description: Optional[str] = None
    """Description of the use policy"""


class FileInstance(BaseModel):
    instance: FileInstanceInstance

    licenses: List[FileInstanceLicense]

    repo_owner: FileInstanceRepoOwner

    repo_revision: FileInstanceRepoRevision

    repository: FileInstanceRepository

    use_policies: List[FileInstanceUsePolicy]


class FileRetrieveResponse(BaseModel):
    first: str
    """Pagination cursor pointing to the first page."""

    next: str
    """Pagination cursor pointing to the next page."""

    prev: str
    """Pagination cursor pointing to the previous page."""

    file_instances: Optional[List[FileInstance]] = None

    last: Optional[str] = None
    """Pagination cursor pointing to the last page."""
