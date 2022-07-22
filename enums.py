from enum import Enum


class TaskPriority(Enum):
    Low = 1
    Medium = 2
    High = 3

class Selector(Enum):
    Task = 'task'
    Tasklist = 'tasklist'
