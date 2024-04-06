from data_structures.lists import IList, DLNode
from typing import TypeVar

T = TypeVar("T")


class DLList(IList[T]):
    def __init__(self, item: T | None = None) -> None:
        self._size = 0
        self._sentinel = DLNode()
        self._sentinel.prev_node = self._sentinel
        self._sentinel.next_node = self._sentinel

        if item is not None:
            node = DLNode(item)

            self._sentinel.prev_node = node
            self._sentinel.next_node = node
            node.prev_node = self._sentinel
            node.next_node = self._sentinel

            self._size = 1

    def add(self, item: T, index: int, _node: DLNode[T] | None = None) -> bool:
        if index < 0 or index > self._size:
            return False

        if _node is None:
            _node = self._sentinel

        if index == 0:
            tmp = _node.next_node

            _node.next_node = DLNode(item)
            _node.next_node.prev_node = _node
            _node.next_node.next_node = tmp
            tmp.prev_node = _node.next_node

            self._size += 1
            return True

        return self.add(item, index - 1, _node.next_node)

    def add_first(self, item: T) -> None:
        self.add(item, 0)

    def add_last(self, item: T) -> None:
        self.add(item, self._size)

    def get(self, index: int, _node: DLNode[T] | None = None) -> T:
        if index < 0 or index >= self._size:
            raise IndexError()

        if _node is None:
            _node = self._sentinel

        if _node.next_node.item is None:
            raise IndexError()

        if index == 0:
            return _node.next_node.item

        return self.get(index - 1, _node.next_node)

    def get_first(self) -> T:
        return self.get(0)

    def remove(self, index: int, _node: DLNode[T] | None = None) -> T:
        if index < 0 or index >= self._size:
            raise IndexError()

        if _node is None:
            _node = self._sentinel

        if _node.next_node.item is None:
            raise IndexError()

        if index == 0:
            if self._size == 1:
                result = _node.next_node.item
                _node.next_node = _node
                _node.prev_node = _node
                self._size -= 1
                return result

            result = _node.next_node.item
            _node.next_node = _node.next_node.next_node
            _node.next_node.prev_node = _node
            self._size -= 1
            return result

        return self.remove(index - 1, _node.next_node)

    def remove_last(self) -> T:
        return self.remove(self._size - 1)

    def size(self) -> int:
        return self._size
