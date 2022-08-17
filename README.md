# tsk

tsk is a task manager CLI written in Python using the `argparse` library and `sqlite3` for data storage. tsk allows you to add, remove, and complete tasks seamlessly.

## Installation
`pip install tsk-official`

## Quickstart
Use the `add` command to add a task to the default tasklist:

`tsk add task 'some task to do'`

Returns:
```
Added task "some task to do" to tasklist "Tasks"
[ ] some task to do--------------------   (kD8Ds)
```
The task id `kD8Ds` is the id to reference the task by later (it will be different for you, of course).

---

Let's use the `complete` command to complete this task (use your task id here instead of kD8Ds):

`tsk complete kD8Ds`

When you list the tasks again with the command `ls`, you will not see the completed task (to show completed tasks type `tsk config View show_completed true`):

`tsk ls`

Returns:
```
Tasks (default_id) (default)
```

---

Adding a new tasklist:

`tsk add tasklist 'some tasklist name'`

Returns:
```
Added tasklist "some tasklist name"
some tasklist name (w9tQq)
```

Use the tasklist id provided (`w9tQq` in my case) and the `-l` flag to link tasks to this tasklist:

`tsk add task 'part of the other tasklist' -l w9tQq`

Returns:
```
Added task "part of the other tasklist" to tasklist "some tasklist name"
[ ] part of the other tasklist---------   (ypost)
```

There are now two tasklists and 1 task:
```
Tasks (default_id) (default)
some tasklist name (w9tQq) 
[ ] part of the other tasklist---------   (ypost)
```

---

To remove a tasklist (and its associated tasks), use the `remove` command (*note that you must specify that you are removing a task and not a tasklist*):

`tsk remove tasklist w9tQq`

You could have removed just the task 'part of the other tasklist' with the command:

`tsk remove task ypost`

---

Let's add a new task but with more information attached. You can add priority, duedate, and notes information to your tasks with simple flags:

`tsk add task 'complex task' -p 3 -d 08/17/22 -n 'this is a note'`

*The duedate must be correctly formatted with padded zeros (format `MM/DD/YY`).*

Returns:
```
Added task "complex task" to tasklist "Tasks"
[ ] complex task----------------------- ! (H8Tij) {...}
      Wed Aug 17
```

This task now has the highest priority (3), a duedate of August 17, 2022, and a note containing 'this is a note'.

---

Additionally, you can update task information with the `update` command:

`tsk update task H8Tij -d 09/09/09 -n 'new note'`

This updates the task's duedate to September 9, 2009 and notes to 'new note'.

## Usage
tsk has 7 commands available:
* `add`
* `complete`
* `remove`
* `update`
* `list`
* `wipe`
* `config`

### add
The `add` command adds a task or tasklist (alternatively use the alias `a`).
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
The `complete` command marks task(s) as complete (alternatively use the alias `cm`).
```
usage: tsk complete [-h] [-u] ids [ids ...]

positional arguments:
  ids               id(s) of the task(s) to complete

optional arguments:
  -h, --help        show this help message and exit
  -u, --uncomplete  undo completion status
```

### remove
The `remove` command removes task(s) or tasklist(s) (alternatively use the alias `rm`).
```
usage: tsk remove [-h] {Selector.Task,Selector.Tasklist} ids [ids ...]

positional arguments:
  {Selector.Task,Selector.Tasklist}
  ids                   id(s) of the task(s)/tasklist(s)

optional arguments:
  -h, --help            show this help message and exit
```

### update
The `update` command updates a task or tasklist (alternatively use the alias `up`).
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
The `list` command displays the tasks of the given tasklist (alternatively use the alias `ls`).
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