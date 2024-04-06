from __future__ import annotations
from data_structures.lists import IList, SLNode
from typing import TypeVar

T = TypeVar("T")


class SLList(IList[T]):

    def __init__(self, item: T | None = None) -> None:
        self._size: int = 0
        self._sentinel: SLNode[T] = SLNode()

        if item is not None:
            self._size = 1
            self._sentinel.next_node = SLNode(item)

    def add(self, item: T, index: int, _node: SLNode | None = None) -> bool:
        if index < 0 or index > self.size():
            return False

        if _node is None:
            _node = self._sentinel

        if index == 0:
            tmp = _node.next_node
            _node.next_node = SLNode(item)
            _node.next_node.next_node = tmp

            self._size += 1
            return True

        return self.add(item, index - 1, _node.next_node)

    def add_first(self, item: T) -> None:
        self.add(item, 0)

    def add_last(self, item: T) -> None:
        self.add(item, self.size())

    def get(self, index: int, _node: SLNode[T] | None = None) -> T:
        if self._sentinel.next_node is None or index < 0 or index >= self.size():
            raise IndexError()

        if _node is None:
            _node = self._sentinel.next_node

        if _node.item is None:
            raise IndexError()

        if index == 0:
            return _node.item

        return self.get(index - 1, _node.next_node)

    def get_first(self) -> T:
        return self.get(0)

    def remove(
        self,
        index: int,
        _node: SLNode[T] | None = None,
        _prev_node: SLNode[T] | None = None,
    ) -> T:
        if self._sentinel.next_node is None or index < 0 or index >= self._size:
            raise IndexError()

        if _node is None:
            _node = self._sentinel.next_node

        if _prev_node is None:
            _prev_node = self._sentinel

        if index == 0:
            if _node is None or _node.item is None:
                raise IndexError()

            _prev_node.next_node = _node.next_node
            self._size -= 1
            return _node.item

        return self.remove(index - 1, _node.next_node, _prev_node.next_node)

    def remove_last(self) -> T:
        return self.remove(self._size - 1)

    def size(self) -> int:
        return self._size
