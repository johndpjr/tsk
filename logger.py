from models.task import Task
from models.tasklist import Tasklist
from enums import TaskPriority
from utils import tstamp_to_friendly_datestr


def print_task(task: Task):
    oput_is_completed = '*' if task.is_completed else ' '
    if task.priority == TaskPriority.High: oput_priority = '!'
    elif task.priority == TaskPriority.Medium: oput_priority = '^'
    elif task.priority == TaskPriority.Low: oput_priority = '.'
    oput_notes = '{...}' if task.notes else ''
    
    print(f'[{oput_is_completed}] {task.title} {oput_priority} {oput_notes}\n'+
          f'      {tstamp_to_friendly_datestr(task.date_due)}'
    )

def print_tasklist(tasklist: Tasklist):
    oput_is_default = '(default)' if tasklist.is_default else ''
    print(f'{tasklist.title} <{tasklist.id}> {oput_is_default}')
