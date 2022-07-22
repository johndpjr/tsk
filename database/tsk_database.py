import sqlite3

from settings import Settings
import utils

from models.task import Task
from models.tasklist import Tasklist


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
