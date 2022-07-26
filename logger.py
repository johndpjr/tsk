from typing import List, Union
from models.task import Task
from models.tasklist import Tasklist
from enums import Selector, TaskPriority
from utils import tstamp_to_friendly_datestr
from settings import Settings


conf = Settings()

def print_tasklist(tasklist: Tasklist):
    """Outputs the tasklist in a pretty format."""

    oput_is_default = '(default)' \
        if tasklist.id == conf['Tasklists']['default_id'] else ''
    print(f'{tasklist.title} ({tasklist.id}) {oput_is_default}')

def print_task(task: Task):
    """Outputs the task in a pretty format"""

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

def feedback_add(selector: Selector, item: Union[Tasklist, Task]):
    """Provides feedback for the "add" command"""

    print(f'Added {selector.name} "{item.title}"')
    if isinstance(item, Tasklist):
        print_tasklist(item)
    else:  # item is Task
        print_task(item)

def feedback_complete(tasks: List[Task], completed: bool):
    """Provides feedback for the "complete" command."""

    oput_complete_msg = 'Completed' if completed else 'Uncompleted'
    task_titles = [task.title for task in tasks]
    print(f'{oput_complete_msg} tasks ', end='')
    for count, title in enumerate(task_titles, 1):
        end_mark = ', ' if count != len(task_titles) else '\n'
        print(f"'{title}'{end_mark}", end='')
