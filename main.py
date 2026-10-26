"""Demonstrate a task manager using a stack, queue, and singly linked list."""

from linkedlist import SinglyLinkedList
from queue import Queue
from stack import Stack
from task import Task


def find_task(tasks: SinglyLinkedList[Task], task_id: int) -> Task | None:
    """Look up a task by its unique ID."""
    return tasks.find(lambda task: task.task_id == task_id)


def add_task(
    tasks: SinglyLinkedList[Task],
    pending_tasks: Queue[int],
    task_id: int,
    description: str,
) -> Task:
    """Save a task and add its ID to the processing queue."""
    task = Task(task_id, description)
    tasks.append(task)
    pending_tasks.enqueue(task_id)
    print(f"Added task {task.task_id}: {task.description}")
    return task


def delete_pending_task(
    tasks: SinglyLinkedList[Task],
    pending_tasks: Queue[int],
    task_id: int,
) -> bool:
    """Cancel a pending task in both the list and the processing queue."""
    task = find_task(tasks, task_id)
    if task is None or task.status != "pending":
        print(f"Task {task_id} was not found as a pending task.")
        return False
    if not pending_tasks.remove(task_id):
        raise RuntimeError(f"Pending task {task_id} was missing from the queue.")
    if not tasks.remove(task):
        raise RuntimeError(f"Task {task_id} could not be removed from the list.")
    print(f"Deleted task {task_id}: {task.description}")
    return True


def process_next_task(
    tasks: SinglyLinkedList[Task],
    pending_tasks: Queue[int],
    completed_tasks: Stack[Task],
) -> Task | None:
    """Complete the next queued task and save it for a possible undo."""
    if pending_tasks.is_empty():
        print("There are no pending tasks to process.")
        return None

    task_id = pending_tasks.dequeue()
    task = find_task(tasks, task_id)
    if task is None or task.status != "pending":
        raise RuntimeError(f"Queued task {task_id} is missing or not pending.")

    task.status = "completed"
    completed_tasks.push(task)
    print(f"Completed task {task.task_id}: {task.description}")
    return task


def undo_last_completion(
    pending_tasks: Queue[int],
    completed_tasks: Stack[Task],
) -> Task | None:
    """Reopen the most recently completed task and queue it again."""
    if completed_tasks.is_empty():
        print("There is no completed task to undo.")
        return None

    task = completed_tasks.pop()
    task.status = "pending"
    pending_tasks.enqueue(task.task_id)
    print(f"Undid completion of task {task.task_id}; it was returned to the queue.")
    return task


def show_tasks(tasks: SinglyLinkedList[Task]) -> None:
    """Display all task records in list order."""
    print("\nTask list:")
    if tasks.is_empty():
        print("  (empty)")
        return
    for task in tasks:
        print(f"  {task.task_id}. [{task.status}] {task.description}")


def run_demo() -> None:
    tasks: SinglyLinkedList[Task] = SinglyLinkedList()
    pending_tasks: Queue[int] = Queue()
    completed_tasks: Stack[Task] = Stack()

    add_task(tasks, pending_tasks, 1, "Review lecture notes")
    add_task(tasks, pending_tasks, 2, "Complete the programming exercise")
    add_task(tasks, pending_tasks, 3, "Email the project group")

    selected_task = find_task(tasks, 2)
    if selected_task is not None:
        print(f"\nRetrieved task 2: {selected_task.description}")

    delete_pending_task(tasks, pending_tasks, 3)
    show_tasks(tasks)

    print("\nProcessing tasks:")
    process_next_task(tasks, pending_tasks, completed_tasks)
    process_next_task(tasks, pending_tasks, completed_tasks)

    print("\nUndoing the last completion:")
    undo_last_completion(pending_tasks, completed_tasks)
    show_tasks(tasks)

    print("\nProcessing the reopened task:")
    process_next_task(tasks, pending_tasks, completed_tasks)
    show_tasks(tasks)


if __name__ == "__main__":
    run_demo()
