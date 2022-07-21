import sqlite3

from models.task import Task
from models.tasklist import Tasklist


class TskDatabase:
    """SQLite Database wrapper for tsk."""

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()

        # Initial table creation sequence
        with self.conn:
            # Create Tasklists table
            self.c.execute("""CREATE TABLE IF NOT EXISTS Tasklists
                (
                    id INTEGER,
                    title TEXT,
                    is_default INTEGER
                )
            """)
            # Create Tasks table
            self.c.execute("""CREATE TABLE IF NOT EXISTS Tasks
                (
                    id INTEGER,
                    tasklist_id TEXT,
                    title TEXT,
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
                    title, priority,
                    date_created, date_due,
                    notes
                )
                VALUES (?,?,?,?,?,?,?)""",
                (
                    task.id, task.tasklist_id,
                    task.title, task.priority,
                    task.date_created, task.date_due,
                    task.notes
                )
            )
