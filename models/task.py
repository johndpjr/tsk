from dataclasses import dataclass
from datetime import datetime

from enums import TaskPriority
import utils


@dataclass
class Task:
    """Models a task - an actionable item to complete."""

    tasklist_id: str
    title: str
    is_completed: bool     = False
    priority: TaskPriority = TaskPriority.Low
    date_created: datetime = datetime.now()
    date_due: datetime     = datetime.now().date()
    notes: str             = ''
    id: str                = utils.get_id()
