from enum import Enum, auto


class TaskPriority(Enum):
    Low = 0
    Medium = 1
    High = 2

class Selector(Enum):
    Task = 'task'
    Tasklist = 'tasklist'
