"""Unit tests for the assignment's data structures."""

import unittest

from linkedlist import SinglyLinkedList
from queue import Queue
from stack import Stack


class StackTests(unittest.TestCase):
    def test_stack_is_last_in_first_out(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_pop_empty_stack_raises(self) -> None:
        with self.assertRaises(IndexError):
            Stack[int]().pop()


class QueueTests(unittest.TestCase):
    def test_queue_is_first_in_first_out(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.is_empty())

    def test_remove_preserves_queue_links(self) -> None:
        queue: Queue[int] = Queue()
        for item in (1, 2, 3):
            queue.enqueue(item)

        self.assertTrue(queue.remove(2))
        self.assertTrue(queue.remove(3))
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 4)
        self.assertFalse(queue.remove(9))

    def test_dequeue_empty_queue_raises(self) -> None:
        with self.assertRaises(IndexError):
            Queue[int]().dequeue()


class SinglyLinkedListTests(unittest.TestCase):
    def test_append_find_remove_and_iteration(self) -> None:
        items: SinglyLinkedList[str] = SinglyLinkedList()
        items.append("first")
        items.append("second")
        items.append("third")

        self.assertEqual(items.find(lambda item: item == "second"), "second")
        self.assertIsNone(items.find(lambda item: item == "missing"))
        self.assertTrue(items.remove("first"))
        self.assertTrue(items.remove("third"))
        self.assertFalse(items.remove("missing"))
        self.assertEqual(list(items), ["second"])

    def test_removing_last_item_resets_list(self) -> None:
        items: SinglyLinkedList[int] = SinglyLinkedList()
        items.append(1)

        self.assertTrue(items.remove(1))
        self.assertTrue(items.is_empty())
        items.append(2)
        self.assertEqual(list(items), [2])


if __name__ == "__main__":
    unittest.main()
