from datetime import datetime

from enums import TaskPriority


def mkdate(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d/%y')

def mkpriority(priority: str) -> TaskPriority:
    return TaskPriority(int(priority))
