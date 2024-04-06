import abc
from typing import TypeVar, Generic

_Item = TypeVar("_Item")


class IList(Generic[_Item], metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add(self, item: _Item, index: int) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_first(self, item: _Item) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_last(self, item: _Item) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, index: int) -> _Item:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_first(self) -> _Item:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, index: int) -> _Item:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_last(self) -> _Item:
        raise NotImplementedError()

    @abc.abstractmethod
    def size(self) -> int:
        raise NotImplementedError()
