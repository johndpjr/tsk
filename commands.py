from argparse import Namespace
from database.tsk_database import TskDatabase

from enums import Selector
from models.task import Task
from models.tasklist import Tasklist
import logger


def add(args: Namespace, db: TskDatabase):
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
        logger.feedback_add(args.selector, task)
    
    elif args.selector == Selector.Tasklist:
        tasklist = Tasklist(args.title)
        db.add_tasklist(tasklist)
        logger.feedback_add(args.selector, tasklist)

def complete(args: Namespace, db: TskDatabase):
    """Complete task(s)."""

    db.set_tasks_completion(args.ids, args.is_set_complete)
    logger.feedback_complete(db.get_tasks_by_ids(args.ids), args.is_set_complete)

def remove(args: Namespace, db: TskDatabase):
    """Remove task(s) or tasklist(s)."""

    if args.selector == Selector.Task:
        db.remove_tasks(args.ids)
    elif args.selector == Selector.Tasklist:
        db.remove_tasklists(args.ids)

def update(args: Namespace, db: TskDatabase):
    """Update task(s) or tasklist(s)."""

    if args.selector == Selector.Task:
        db.update_task(
            args.id,
            title=args.title,
            priority=args.task_priority,
            notes=args.task_notes
        )
    elif args.selector == Selector.Tasklist:
        db.update_tasklist(
            args.id,
            title=args.title
        )

def list(args: Namespace, db: TskDatabase):
    """List tasks(s) or tasklist(s)."""
    
    if args.tasklist_id:
        tasklist = db.get_tasklists([args.tasklist_id])
        if tasklist:
            tasklist = tasklist[0]
            logger.print_tasklist(tasklist)
            tasks = db.get_tasks(args.tasklist_id)
            for task in tasks:
                logger.print_task(task)
            
    else:  # print all the tasklists if no id was specified
        tasklists = db.get_tasklists()
        for tasklist in tasklists:
            logger.print_tasklist(tasklist)
            tasks = db.get_tasks(tasklist.id)
            for task in tasks:
                logger.print_task(task)

def wipe(args: Namespace, db: TskDatabase):
    """Remove all tasklists and tasks."""

    resp = input('Remove all tasklists and tasks? [Y/n] ')
    if not resp or resp.lower() == 'y':
        db.wipe()
        print('Removed all tasklists and tasks')
