"""A node-based first-in, first-out queue."""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class _QueueNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next: _QueueNode[T] | None = None


class Queue(Generic[T]):
    """Store items so the earliest enqueued item is removed first."""

    def __init__(self) -> None:
        self._head: _QueueNode[T] | None = None
        self._tail: _QueueNode[T] | None = None
        self._size = 0

    def enqueue(self, item: T) -> None:
        """Add an item to the back of the queue."""
        node = _QueueNode(item)
        if self._tail is None:
            # The first node is both the front and the back of the queue.
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def dequeue(self) -> T:
        """Remove and return the item at the front of the queue."""
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        item = self._head.value
        self._head = self._head.next
        self._size -= 1
        if self._head is None:
            # Keep both ends empty after removing the final node.
            self._tail = None
        return item

    def peek(self) -> T:
        """Return the front item without removing it."""
        if self._head is None:
            raise IndexError("peek at empty queue")
        return self._head.value

    def remove(self, item: T) -> bool:
        """Remove the first matching item, returning whether it was found."""
        previous: _QueueNode[T] | None = None
        current = self._head

        while current is not None:
            if current.value == item:
                # Link around the match without disturbing the other queued items.
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
        """Return whether the queue has no items."""
        return self._size == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return self._size

    def __len__(self) -> int:
        return self.size()
