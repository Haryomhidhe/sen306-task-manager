"""A simple last-in, first-out stack."""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Store items so the most recently added item is removed first."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        # List append and pop at the end implement last-in, first-out behavior.
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return whether the stack has no items."""
        return not self._items

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)

    def __len__(self) -> int:
        return self.size()
