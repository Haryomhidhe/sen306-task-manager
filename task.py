"""Task record used by the task manager demonstration."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class Task:
    task_id: int
    description: str
    status: Literal["pending", "completed"] = "pending"
