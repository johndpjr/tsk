from argparse import Namespace
from database.tsk_database import TskDatabase

from enums import Selector
from models.task import Task
from models.tasklist import Tasklist
from settings import Settings
import logger


def add(args: Namespace, conf: Settings, db: TskDatabase):
    """Add task(s) or tasklist(s)."""

    if args.selector == Selector.Task:
        task = Task(
            args.tasklist_id,
            args.title,
            priority=args.task_priority,
            date_due=args.task_date_due,
            notes=args.task_notes
        )
        db.add_task(task)
        print('Added task')
        logger.print_task(task)
    
    elif args.selector == Selector.Tasklist:
        tasklist = Tasklist(args.title)
        db.add_tasklist(tasklist)
        print('Added tasklist')
        logger.print_tasklist(tasklist)

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
    
    if args.all:
        tasklists = db.get_tasklists()
        for tasklist in tasklists:
            logger.print_tasklist(tasklist)
            tasks = db.get_tasks(tasklist.id)
            for task in tasks:
                logger.print_task(task)
    if args.id:
        tasklists = db.get_tasklists(args.id)
        for tasklist in tasklists:
            logger.print_tasklist(tasklist)
            tasks = db.get_tasks(tasklist.id)
            for task in tasks:
                logger.print_task(task)
