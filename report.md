# SEN 306 Software Construction — Task Manager

**Name:** ____________________  
**Registration number:** ____________________  
**Date:** ____________________

## Task summary

This project is a small Python task manager demonstrating a stack, a queue, and a singly linked list in a practical workflow. Tasks can be added, retrieved by ID, cancelled while pending, processed, and reopened by undoing the latest completion. Run the example with `python main.py`.

## Use of the data structures

- **Singly linked list (`linkedlist.py`):** stores task records in insertion order. Its append, find, and remove operations support adding, retrieving, displaying, and cancelling tasks.
- **Queue (`queue.py`):** stores IDs of pending tasks. Tasks are processed in first-in, first-out order. Its remove operation also lets the application cancel a pending task without leaving a stale ID in the queue.
- **Stack (`stack.py`):** stores completed tasks. The most recently completed task is on top, so undo reopens the latest completion first and puts it at the end of the pending queue.

## Software construction principles

Each data structure and the `Task` record has its own module, separating reusable logic from the demonstration in `main.py`. Classes and methods have focused responsibilities, descriptive names, type annotations, and docstrings. The task manager composes the three structures through their public methods rather than depending on their internal nodes. Empty stack and queue operations raise clear `IndexError` exceptions; application-level inconsistencies raise `RuntimeError`. Unit tests in `test_data_structures.py` check ordering, removal, lookup, and empty-state behavior.
