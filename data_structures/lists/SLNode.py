from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")


class SLNode(Generic[T]):

    def __init__(self, item: T | None = None, next_node: SLNode | None = None) -> None:
        self.item = item
        self.next_node = next_node
