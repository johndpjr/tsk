from typing import List
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
    
    task_oput = f'[{oput_is_completed}] ' \
                f'{task.title:-<35} ' \
                f'{oput_priority} ' \
                f'({task.id}) ' \
                f'{oput_notes}\n' \
                f'      {tstamp_to_friendly_datestr(task.date_due)}'
    print(task_oput)

def print_tasklist(tasklist: Tasklist):
    oput_is_default = '(default)' if tasklist.is_default else ''
    print(f'{tasklist.title} ({tasklist.id}) {oput_is_default}')

def feedback_complete(tasks: List[Task], completed: bool):
    """Provides feedback for the 'complete' command."""
    oput_complete_msg = 'Completed' if completed else 'Uncompleted'
    task_titles = [task.title for task in tasks]
    print(f'{oput_complete_msg} tasks ', end='')
    for count, title in enumerate(task_titles, 1):
        end_mark = ', ' if count != len(task_titles) else '\n'
        print(f"'{title}'{end_mark}", end='')
