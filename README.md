# tsk

tsk is a task manager CLI written in Python using the `argparse` library and `sqlite3` for data storage. tsk allows you to add, remove, and complete tasks seamlessly.

## Installation
TODO

## Usage
tsk has 6 commands available:
* `add`
* `complete`
* `remove`
* `update`
* `list`
* `wipe`

### add
The `add` command adds a task or tasklist.
```
usage: tsk add [-h] [-l TASKLIST_ID] [-p {1,2,3}] [-d TASK_DATE_DUE]
               [-n TASK_NOTES]
               {Selector.Task,Selector.Tasklist} title

positional arguments:
  {Selector.Task,Selector.Tasklist}
  title                 name of the task

optional arguments:
  -h, --help            show this help message and exit
  -l TASKLIST_ID        id of the tasklist to add the task to
  -p {1,2,3}, --priority {1,2,3}
                        priority of the task
  -d TASK_DATE_DUE, --duedate TASK_DATE_DUE
                        date the task should be completed by
  -n TASK_NOTES, --notes TASK_NOTES
                        additional task information
```

### complete
The `complete` command marks task(s) as complete.
```
usage: tsk complete [-h] [-u] ids [ids ...]

positional arguments:
  ids               id(s) of the task(s) to complete

optional arguments:
  -h, --help        show this help message and exit
  -u, --uncomplete  undo completion status
```

### remove
The `remove` command removes task(s) or tasklist(s).
```
usage: tsk remove [-h] {Selector.Task,Selector.Tasklist} ids [ids ...]

positional arguments:
  {Selector.Task,Selector.Tasklist}
  ids                   id(s) of the task(s)/tasklist(s)

optional arguments:
  -h, --help            show this help message and exit
```

### update
The `update` command updates a task or tasklist.
```
usage: tsk update [-h] [-t TITLE] [--make-default] [-p {1,2,3}]
                  [-d TASK_DATE_DUE] [-n TASK_NOTES]
                  {Selector.Task,Selector.Tasklist} id

positional arguments:
  {Selector.Task,Selector.Tasklist}
  id                    id of the task/tasklist to update

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        name of the task/tasklist
  --make-default        make this tasklist the default tasklist
  -p {1,2,3}, --priority {1,2,3}
                        priority of the task
  -d TASK_DATE_DUE, --duedate TASK_DATE_DUE
                        date the task should be completed by
  -n TASK_NOTES, --notes TASK_NOTES
                        additional task information
```

### list
The `list` command displays the tasks of the given tasklist.
```
usage: tsk list [-h] [tasklist_id]

positional arguments:
  tasklist_id  id of the tasklist

optional arguments:
  -h, --help   show this help message and exit
```

### wipe
The `wipe` command **permanently clears** *all* tasks and tasklists. It will ask the user for confirmation.
```
usage: tsk wipe [-h]

optional arguments:
  -h, --help  show this help message and exit
```

### config
The `config` command configures task defaults and view options.
The following options can be configured:
* `TaskDefaults`
  * `tasklist_id` is the default id of the tasklist assigned to every task that does not explicitly define a tasklist through the `-l` flag
  * `priority` is the default task priority that uses the integers 1-3 to indicate importance (*use 0 for no default `priority`*)
  * `date_due` is the default duedate of the task, measured in days from today [0 for today, 1 for tomorrow, etc.] (*use -1 for no default `date_due`*)
* `View`
  * `show_completed` is either `true` or `false`; it determines if completed tasks are shown when listing tasks
```
usage: tsk config [-h] {TaskDefaults,View} key value

positional arguments:
  {TaskDefaults,View}
  key
  value

options:
  -h, --help           show this help message and exit
```