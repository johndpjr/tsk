from argparse import Namespace
from database.tsk_database import TskDatabase

from enums import Selector
from models.task import Task
from models.tasklist import Tasklist
from settings import Settings


def add(args: Namespace, conf: Settings, db: TskDatabase):
    """Add task(s) or tasklist(s)."""

    print(args)

    if args.selector == Selector.Task:
        task = Task(
            args.tasklist_id,
            args.title,
            priority=args.task_priority,
            date_due=args.task_date_due,
            notes=args.task_notes
        )
        print(task)
        db.add_task(task)
    
    elif args.selector == Selector.Tasklist:
        tasklist = Tasklist(args.title)
        print(tasklist)
        db.add_tasklist(tasklist)

def complete(args: Namespace, conf: Settings, db: TskDatabase):
    """Complete task(s)."""
    pass

def remove(args: Namespace, conf: Settings, db: TskDatabase):
    """Remove task(s) or tasklist(s)."""
    pass

def update(args: Namespace, conf: Settings, db: TskDatabase):
    """Update task(s) or tasklist(s)."""
    pass

def list(args: Namespace, conf: Settings, db: TskDatabase):
    """List tasks(s) or tasklist(s)."""
    pass
