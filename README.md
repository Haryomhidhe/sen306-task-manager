# SEN 306 Task Manager

A small Python task manager demonstrating a stack, a queue, and a singly linked list.

## Run the demo

```bash
python main.py
```

## Run the tests

```bash
python -m unittest -v test_data_structures
```

## Data structures

- `linkedlist.py` stores task records and supports lookup and cancellation.
- `queue.py` schedules pending tasks in first-in, first-out order.
- `stack.py` tracks completed tasks so the latest completion can be undone.
- `task.py` defines the task record.
- `main.py` demonstrates adding, retrieving, deleting, processing, and undoing tasks.

See [report.md](report.md) for the assignment summary and software construction principles.
