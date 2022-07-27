import argparse

import parsers
from database.tsk_database import TskDatabase
from settings import Settings

conf = Settings()

parser = argparse.ArgumentParser(
    prog='tsk',
    description='add, remove, and complete tasks seamlessly'
)

subparser = parser.add_subparsers(dest='command')

# add: adds a task
parsers.construct(subparser, 'add', aliases=['a'])

# complete: marks a task as completed
parsers.construct(subparser, 'complete', aliases=['cm'])

# remove: deletes task(s)/tasklist(s)
parsers.construct(subparser, 'remove', aliases=['rm'])

# update: update task/tasklist data
parsers.construct(subparser, 'update', aliases=['up'])

# list: list tasklist(s) data
parsers.construct(subparser, 'list', aliases=['ls'])

# wipe: remove all tasklists and tasks
parsers.construct(subparser, 'wipe')


# parse args
args = parser.parse_args()

tsk_db = TskDatabase()
args.func(args, tsk_db)
