"""Task record used by the task manager demonstration."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class Task:
    """Keep task identity, display text, and workflow status together."""

    task_id: int
    description: str
    status: Literal["pending", "completed"] = "pending"
