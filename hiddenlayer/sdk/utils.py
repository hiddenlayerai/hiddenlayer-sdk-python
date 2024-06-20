import os
from fnmatch import fnmatch
from pathlib import Path
from typing import Generator, List, Optional, Union
from urllib.parse import urlparse

PathInputType = Union[str, os.PathLike]


def filter_path_objects(
    items: Union[List[PathInputType], Generator[PathInputType, None, None]],
    *,
    allow_patterns: Optional[Union[List[str], str]] = None,
    ignore_patterns: Optional[Union[List[str], str]] = None,
) -> Generator[Union[str, os.PathLike], None, None]:
    """Filter repo objects based on an allowlist and a denylist.

    Input must be a list of paths (`str` or `Path`) or a list of arbitrary objects.
    In the later case, `key` must be provided and specifies a function of one argument
    that is used to extract a path from each element in iterable.

    Patterns are Unix shell-style wildcards which are NOT regular expressions. See
    https://docs.python.org/3/library/fnmatch.html for more details.

    :param items: List of paths to filter.
    :param allow_patterns: Patterns constituting the allowlist. If provided, item paths must match at
            least one pattern from the allowlist.
    :param ignore_patterns: Patterns constituting the denylist. If provided, item paths must not match
            any patterns from the denylist.

    :returns: Filtered list of objects, as a generator.

    :raises:
        :class:`ValueError`:
            If `key` is not provided and items are not `str` or `Path`.

    Example usage with paths:
    ```python
    >>> # Filter only PDFs that are not hidden.
    >>> list(filter_repo_objects(
    ...     ["aaa.PDF", "bbb.jpg", ".ccc.pdf", ".ddd.png"],
    ...     allow_patterns=["*.pdf"],
    ...     ignore_patterns=[".*"],
    ... ))
    ["aaa.pdf"]
    ```
    """
    if isinstance(allow_patterns, str):
        allow_patterns = [allow_patterns]

    if isinstance(ignore_patterns, str):
        ignore_patterns = [ignore_patterns]

    def _identity(item: Union[str, os.PathLike]) -> Path:
        if isinstance(item, str):
            return Path(item)
        if isinstance(item, Path):
            return item
        raise ValueError("Objects must be string or Pathlike.")

    key = _identity  # Items must be `str` or `Path`, otherwise raise ValueError

    for item in items:
        path: Path = key(item)

        if path.is_dir():
            continue

        # Skip if there's an allowlist and path doesn't match any
        if allow_patterns is not None and not any(
            fnmatch(str(path), r) for r in allow_patterns
        ):
            continue

        # Skip if there's a denylist and path matches any
        if ignore_patterns is not None and any(
            fnmatch(str(path), r) for r in ignore_patterns
        ):
            continue

        yield item


def is_saas(host: str) -> bool:
    """Checks whether the connection is to the SaaS platform"""

    o = urlparse(host)

    if o.hostname and o.hostname.endswith("hiddenlayer.ai"):
        return True

    return False
