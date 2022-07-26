import argparse
from datetime import datetime

import commands
import transforms
import utils
from database.tsk_database import TskDatabase
from enums import Selector, TaskPriority
from settings import Settings

conf = Settings()

parser = argparse.ArgumentParser(
    prog='tsk',
    description='add, remove, and complete tasks seamlessly'
)

subparser = parser.add_subparsers(dest='command')

# add: adds a task
command_add = subparser.add_parser('add', aliases=['a'])
command_add.add_argument('selector', type=Selector,
                         choices=[s for s in Selector])
command_add.add_argument('title', type=str,
                         help='name of the task')
command_add.add_argument('-l', type=str,
                         default=conf['Tasklists']['default_id'],
                         dest='tasklist_id',
                         help='id of the tasklist to add the task to')
command_add.add_argument('-p', '--priority', type=transforms.mkpriority,
                         default=TaskPriority.Medium,
                         choices=list(TaskPriority),
                         dest='task_priority',
                         help='priority of the task')
command_add.add_argument('-d', '--duedate', type=transforms.mkdate,
                         dest='task_date_due',
                         default=utils.tstamp_to_american_datestr(datetime.now().date()),
                         help='date the task should be completed by')
command_add.add_argument('-n', '--notes', type=str,
                         default='',
                         dest='task_notes',
                         help='additional task information')
command_add.set_defaults(func=commands.add)

# complete: marks a task as completed
command_complete = subparser.add_parser('complete', aliases=['cm'])
command_complete.add_argument('ids', type=str,
                              nargs='+',
                              help='id(s) of the task(s) to complete')
command_complete.add_argument('-u', '--uncomplete', action='store_false',
                              dest='is_set_complete',
                              help='undo completion status')
command_complete.set_defaults(func=commands.complete)

# remove: deletes task(s)/tasklist(s)
command_remove = subparser.add_parser('remove', aliases=['rm'])
command_remove.add_argument('selector', type=Selector,
                            choices=[s for s in Selector])
command_remove.add_argument('ids', type=str,
                            nargs='+',
                            help='id(s) of the task(s)/tasklist(s)')
command_remove.set_defaults(func=commands.remove)

# update: update task/tasklist data
command_update = subparser.add_parser('update', aliases=['up'])
command_update.add_argument('selector', type=Selector,
                            choices=[s for s in Selector])
command_update.add_argument('id', type=str,
                            help='id of the task/tasklist to update')
command_update.add_argument('-t', '--title', type=str,
                            help='name of the task/tasklist')
command_update.add_argument('--make-default', action='store_true',
                            dest='tasklist_default',
                            help='make this tasklist the default tasklist')
command_update.add_argument('-p', '--priority', type=transforms.mkpriority,
                            choices=list(TaskPriority),
                            dest='task_priority',
                            help='priority of the task')
command_update.add_argument('-d', '--duedate', type=transforms.mkdate,
                            dest='task_date_due',
                            help='date the task should be completed by')
command_update.add_argument('-n', '--notes', type=str,
                            dest='task_notes',
                            help='additional task information')
command_update.set_defaults(func=commands.update)

# list: list tasklist(s) data
command_list = subparser.add_parser('list', aliases=['ls'])
command_list.add_argument('tasklist_id', type=str,
                          nargs='?',
                          help='id of the tasklist')
command_list.set_defaults(func=commands.list)

# wipe: remove all tasklists and tasks
command_wipe = subparser.add_parser('wipe')
command_wipe.set_defaults(func=commands.wipe)


# Parse args
args = parser.parse_args()

tsk_db = TskDatabase()
args.func(args, tsk_db)
