from argparse import ArgumentParser
from datetime import datetime

from enums import Selector, TaskPriority
import transforms
import utils
from settings import Settings
import commands


conf = Settings()

def construct(subparser, name: str, **kwargs):
    # create base parser with name and aliases
    base_parser = subparser.add_parser(name, **kwargs)

    # add arguments to the base parser
    # link the command to a function
    if name == 'add':
        _construct_add_parser(base_parser)
        base_parser.set_defaults(func=commands.add)
    elif name == 'complete':
        _construct_complete_parser(base_parser)
        base_parser.set_defaults(func=commands.complete)
    elif name == 'remove':
        _construct_remove_parser(base_parser)
        base_parser.set_defaults(func=commands.remove)
    elif name == 'update':
        _construct_update_parser(base_parser)
        base_parser.set_defaults(func=commands.update)
    elif name == 'list':
        _construct_list_parser(base_parser)
        base_parser.set_defaults(func=commands.list)
    elif name == 'wipe':
        _construct_wipe_parser(base_parser)
        base_parser.set_defaults(func=commands.wipe)

def _construct_add_parser(p: ArgumentParser):
    p.add_argument('selector', type=Selector,
                   choices=[s for s in Selector])
    p.add_argument('title', type=str,
                   help='name of the task')
    p.add_argument('-l', type=str,
                   default=conf['Tasklists']['default_id'],
                   dest='tasklist_id',
                   help='id of the tasklist to add the task to')
    p.add_argument('-p', '--priority', type=transforms.mkpriority,
                   default=TaskPriority.Medium,
                   choices=list(TaskPriority),
                   dest='task_priority',
                   help='priority of the task')
    p.add_argument('-d', '--duedate', type=transforms.mkdate,
                   dest='task_date_due',
                   default=utils.tstamp_to_american_datestr(datetime.now().date()),
                   help='date the task should be completed by')
    p.add_argument('-n', '--notes', type=str,
                   default='',
                   dest='task_notes',
                   help='additional task information')

def _construct_complete_parser(p: ArgumentParser):
    p.add_argument('ids', type=str,
                   nargs='+',
                   help='id(s) of the task(s) to complete')
    p.add_argument('-u', '--uncomplete', action='store_false',
                   dest='is_set_complete',
                   help='undo completion status')

def _construct_remove_parser(p: ArgumentParser):
    p.add_argument('selector', type=Selector,
                   choices=[s for s in Selector])
    p.add_argument('ids', type=str,
                   nargs='+',
                   help='id(s) of the task(s)/tasklist(s)')

def _construct_update_parser(p: ArgumentParser):
    p.add_argument('selector', type=Selector,
                   choices=[s for s in Selector])
    p.add_argument('id', type=str,
                   help='id of the task/tasklist to update')
    p.add_argument('-t', '--title', type=str,
                   help='name of the task/tasklist')
    p.add_argument('--make-default', action='store_true',
                   dest='tasklist_default',
                   help='make this tasklist the default tasklist')
    p.add_argument('-p', '--priority', type=transforms.mkpriority,
                   choices=list(TaskPriority),
                   dest='task_priority',
                   help='priority of the task')
    p.add_argument('-d', '--duedate', type=transforms.mkdate,
                   dest='task_date_due',
                   help='date the task should be completed by')
    p.add_argument('-n', '--notes', type=str,
                   dest='task_notes',
                   help='additional task information')

def _construct_list_parser(p: ArgumentParser):
    p.add_argument('tasklist_id', type=str,
                   nargs='?',
                   help='id of the tasklist')

def _construct_wipe_parser(p: ArgumentParser):
    pass
