"""A generic singly linked list."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next: _Node[T] | None = None


class SinglyLinkedList(Generic[T]):
    """Maintain an ordered collection of values using singly linked nodes."""

    def __init__(self) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0

    def append(self, value: T) -> None:
        """Add a value to the end of the list."""
        node = _Node(value)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def find(self, predicate: Callable[[T], bool]) -> T | None:
        """Return the first value matching a predicate, or None if absent."""
        current = self._head
        while current is not None:
            if predicate(current.value):
                return current.value
            current = current.next
        return None

    def remove(self, value: T) -> bool:
        """Remove the first matching value, returning whether it was found."""
        previous: _Node[T] | None = None
        current = self._head

        while current is not None:
            if current.value == value:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                if current is self._tail:
                    self._tail = previous
                self._size -= 1
                if self._head is None:
                    self._tail = None
                return True
            previous = current
            current = current.next
        return False

    def is_empty(self) -> bool:
        """Return whether the list has no values."""
        return self._size == 0

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size
