import argparse
from datetime import datetime

from enums import Selector, TaskPriority
import commands
import utils
import transforms
from database.tsk_database import TskDatabase

from settings import Settings

conf = Settings()

parser = argparse.ArgumentParser(
    prog='tsk',
    description='add, remove, and complete tasks seamlessly')

subparser = parser.add_subparsers(dest='command')

# Add: adds a task 
command_add = subparser.add_parser('add', aliases=['a'])
command_add.add_argument('selector', type=Selector,
                         choices=[s for s in Selector])
command_add.add_argument('--tasklist-id', type=str,
                         default=conf['Tasklists']['default_id'],
                         dest='tasklist_id',
                         help='id of the tasklist you add task to')
command_add.add_argument('-t', '--title', required=True, type=str,
                         help='name of the task')
command_add.add_argument('-p', '--priority', type=transforms.mkpriority,
                         default=TaskPriority.Medium,
                         choices=list(TaskPriority),
                         dest='task_priority',
                         help='priority of the task')
command_add.add_argument('-d', '--duedate', type=transforms.mkdate,
                         dest='task_date_due',
                         default=utils.tstamp_to_datestr(datetime.now().date()),
                         help='date the task should be completed by')
command_add.add_argument('-n', '--notes', type=str,
                         default='',
                         dest='task_notes',
                         help='additional task information')
command_add.set_defaults(func=commands.add)

# Complete: marks a task as done
command_complete = subparser.add_parser('complete', aliases=['cm'])
command_complete.set_defaults(func=commands.complete)

# Remove: deletes task(s)/tasklist(s)
command_remove = subparser.add_parser('remove', aliases=['rm'])
command_remove.set_defaults(func=commands.remove)

# Update: update task/tasklist data
command_update = subparser.add_parser('update', aliases=['up'])
command_update.set_defaults(func=commands.update)

# List: list tasks/tasklists data
command_list = subparser.add_parser('list', aliases=['ls'])
command_list.set_defaults(func=commands.list)


# Parse args
args = parser.parse_args()

tsk_db = TskDatabase()
args.func(args, conf, tsk_db)
