import argparse

from enums import Selector
import commands
from database.tsk_database import TskDatabase


parser = argparse.ArgumentParser(
    prog='tsk',
    description='add, remove, and complete tasks seamlessly')

subparser = parser.add_subparsers(dest='command')

# Add
command_add = subparser.add_parser('add', aliases=['a'])
command_add.add_argument('selector', type=Selector,
                         choices=[Selector.Task,
                                  Selector.Tasklist])
command_add.add_argument('-t', '--title', required=True, type=str)
command_add.set_defaults(func=commands.add)

# Complete
command_complete = subparser.add_parser('complete', aliases=['cm'])
command_complete.set_defaults(func=commands.complete)

# Remove
command_remove = subparser.add_parser('remove', aliases=['rm'])
command_remove.set_defaults(func=commands.remove)

# Update
command_update = subparser.add_parser('update', aliases=['up'])
command_update.set_defaults(func=commands.update)

# List
command_list = subparser.add_parser('list', aliases=['ls'])
command_list.set_defaults(func=commands.list)


# Parse args
args = parser.parse_args()

tsk_db = TskDatabase()
args.func(args, tsk_db)
