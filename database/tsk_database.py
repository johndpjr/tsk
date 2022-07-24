import sqlite3
from typing import List

from settings import Settings
import utils

from models.task import Task
from models.tasklist import Tasklist
from enums import TaskPriority


class TskDatabase:
    """SQLite Database wrapper for tsk."""

    def __init__(self):
        self.conf = Settings()
        self.conn = sqlite3.connect(self.conf['Database']['filename'])
        self.c = self.conn.cursor()

        # Initial table creation sequence
        with self.conn:
            self._create_tasklists_table()
            self._add_default_tasklist_ifndef()
            self._create_tasks_table()
    
    def _create_tasklists_table(self):
        """Add a Tasklists table to the Database if it doesn't exist.
        - Columns:
            * id         (str) : tasklist id
            * title      (str) : name of the tasklist
            * is_default (bool): indicates if default tasklist
        """

        self.c.execute("""CREATE TABLE IF NOT EXISTS Tasklists
            (
                id TEXT,
                title TEXT,
                is_default INTEGER
            )
        """)
    
    def _add_default_tasklist_ifndef(self):
        """Add the default tasklist to the Tasklists table if
        there are no rows.
        """

        num_rows = self.c.execute("""
            SELECT COUNT(*) FROM Tasklists
        """).fetchone()[0]
        if not num_rows:
            default_tasklist = Tasklist(
                title='Tasks',
                is_default=True,
                id='default_id'
            )
            self.add_tasklist(default_tasklist)
            self.conf['Tasklists']['default_id'] = default_tasklist.id
    
    def _create_tasks_table(self):
        """Add a Tasks table to the Database if it doesn't exist.
        - Columns:
            * id           (str): task id
            * tasklist_id  (str): parent tasklist id
            * title        (str): task name
            * is_completed (bool): indicates if the task is finished
            * priority     (int): 1-3 importance rank (1 lowest / 3 highest)
            * date_created (str): task creation date timestamp
            * date_due     (str): date the task should be completed by
            * notes        (str): additional task information
        """
        
        self.c.execute("""CREATE TABLE IF NOT EXISTS Tasks
            (
                id TEXT,
                tasklist_id TEXT,
                title TEXT,
                is_completed INTEGER,
                priority INTEGER,
                date_created TEXT,
                date_due TEXT,
                notes TEXT
            )
        """)
    
    def _transform_tasklist(self, tasklist_data) -> Tasklist:
        tasklist = Tasklist(
            title=tasklist_data[1],
            is_default=tasklist_data[2],
            id=tasklist_data[0]
        )
        return tasklist

    def _transform_task(self, task_data) -> Task:
        task = Task(
            tasklist_id=task_data[1],
            title=task_data[2],
            is_completed=task_data[3],
            priority=TaskPriority(task_data[4]),
            date_created=utils.tstr_to_tstamp(task_data[5]),
            date_due=utils.tstr_to_tstamp(task_data[6]),
            notes=task_data[7],
            id=task_data[0],
        )
        return task
    
    def add_tasklist(self, tasklist: Tasklist):
        """Adds a tasklist to the database."""
        with self.conn:
            self.c.execute("""INSERT INTO Tasklists
                (
                    id, title, is_default
                )
                VALUES (?,?,?)""",
                (
                    tasklist.id, tasklist.title, tasklist.is_default
                )
            )
    
    def add_task(self, task: Task):
        """Adds a task to the database."""
        with self.conn:
            self.c.execute("""INSERT INTO Tasks
                (
                    id, tasklist_id,
                    title, is_completed,
                    priority, date_created,
                    date_due, notes
                )
                VALUES (?,?,?,?,?,?,?,?)""",
                (
                    task.id, task.tasklist_id,
                    task.title, task.is_completed,
                    task.priority.value,
                    utils.tstamp_to_tstr(task.date_created),
                    utils.tstamp_to_tstr(task.date_due),
                    task.notes
                )
            )

    def get_tasklists(self, query_ids: List[str]=[]) -> List[Tasklist]:
        """Returns a list of all tasklists."""

        tasklists = []
        if query_ids:
            for query_id in query_ids:
                self.c.execute("""
                    SELECT * FROM Tasklists WHERE id=?
                """, (query_id,))
                qres = self.c.fetchone()
                if qres is None:
                    print('No tasks found')
                else:
                    tasklists.append(self._transform_tasklist(qres))
        else:
            self.c.execute("""
                SELECT * FROM Tasklists
            """)
            res = self.c.fetchall()
            if res:
                [tasklists.append(self._transform_tasklist(tasklist_data)) for tasklist_data in res]
        
        return tasklists

    def get_tasks(self, tasklist_id: str) -> List[Task]:
        """Returns a list of Tasks that are in the Tasklist.
        If no Tasks match the Tasklist or if the id doesn't exist,
        an empty list is returned.
        """

        self.c.execute("""
            SELECT * FROM Tasks WHERE tasklist_id=?
        """, (tasklist_id,))
        res = self.c.fetchall()
        if res:
            tasks = [self._transform_task(task_data) for task_data in res]
            return tasks
        return []

    def complete_tasks(self, ids: List[str]):
        """Sets is_completed for all tasks in ids."""
        
        ids = [[id] for id in ids]
        with self.conn:
            self.c.executemany("""
                UPDATE Tasks SET is_completed=TRUE WHERE id=(?)
            """, ids)

    def remove_tasklists(self, tasklist_ids: List[str]):
        """Removes all tasklists with matching ids. Also deletes all
        tasks within the matching tasklists.
        """
        tasklist_ids = [(id,) for id in tasklist_ids]
        with self.conn:
            # Delete tasklists
            self.c.executemany("""
                DELETE FROM Tasklists WHERE id=?
            """, tasklist_ids)
            # Delete tasks associated with tasklists
            self.c.executemany("""
                DELETE FROM Tasks WHERE tasklist_id=?
            """, tasklist_ids)

    def remove_tasks(self, ids: List[str]):
        """Removes all tasks with matching ids."""
        ids = [(id,) for id in ids]
        with self.conn:
            self.c.executemany("""
                DELETE FROM Tasks WHERE id=?
            """, ids)
