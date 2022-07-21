from argparse import Namespace
from database.tsk_database import TskDatabase

from enums import Selector
from models.task import Task
from models.tasklist import Tasklist


def add(args: Namespace, db: TskDatabase):
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
        db.add_task(task)
    
    elif args.selector == Selector.Tasklist:
        tasklist = Tasklist(args.title)
        db.add_tasklist(tasklist)

def complete(args: Namespace, db: TskDatabase):
    """Complete task(s)."""
    pass

def remove(args: Namespace, db: TskDatabase):
    """Remove task(s) or tasklist(s)."""
    pass

def update(args: Namespace, db: TskDatabase):
    """Update task(s) or tasklist(s)."""
    pass

def list(args: Namespace, db: TskDatabase):
    """List tasks(s) or tasklist(s)."""
    pass
