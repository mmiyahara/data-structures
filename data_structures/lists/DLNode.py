from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")


class DLNode(Generic[T]):
    def __init__(
        self,
        item: T | None = None,
        prev_node: DLNode | None = None,
        next_node: DLNode | None = None,
    ) -> None:
        self.item = item
        if prev_node is None or next_node is None:
            self.prev_node = self
            self.next_node = self
