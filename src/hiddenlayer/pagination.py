# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPaginationPage", "SyncCursorPagination", "AsyncCursorPagination"]

_T = TypeVar("_T")


class CursorPaginationPage(BaseModel):
    next: Optional[str] = None

    prev: Optional[str] = None


class SyncCursorPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page: Optional[CursorPaginationPage] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next = None
        if self.page is not None:
            if self.page.next is not None:
                next = self.page.next
        if not next:
            return None

        return PageInfo(params={"cursor": next})


class AsyncCursorPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page: Optional[CursorPaginationPage] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next = None
        if self.page is not None:
            if self.page.next is not None:
                next = self.page.next
        if not next:
            return None

        return PageInfo(params={"cursor": next})
