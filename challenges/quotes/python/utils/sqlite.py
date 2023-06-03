# coding: utf-8
"""Module for an SQLite db of indexed document."""
import logging
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Iterator, List


class SqliteDb:
    """Base class to work with SQLite db."""

    def __init__(self, db_path: Path, sql: str):
        """Initialize.

        sql is the DDL SQL to create the database.
        """
        self.path = db_path
        if not db_path.exists():
            self.create_db(sql)

    @staticmethod
    def _dict_factory(cursor, row):
        """Define dict as return value for query."""
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    @contextmanager
    def _get_auto_conn(self) -> Iterator[sqlite3.Cursor]:
        """Return a cursor of an autocommit autoclose connection with dict factory."""
        conn = sqlite3.connect(
            self.path,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        conn.row_factory = self._dict_factory
        cur = conn.cursor()

        try:
            yield cur
        except sqlite3.Error as error:
            logging.error("SQLite error: %s", error)
            raise
        finally:
            conn.commit()
            conn.close()

    def create_db(self, sql: str):
        """Create db with the given SQL query.

        sql is the DDL SQL to create the database.
        Call exucutescript to support muli-statement SQL.
        """
        with self._get_auto_conn() as conn:
            conn.executescript(sql)
            logging.info("SQLite db %s created", self.path)

    def fetchone(self, sql: str, params: tuple) -> Dict:
        """Get an entry from db matching a query."""
        with self._get_auto_conn() as conn:
            res = conn.execute(sql, params)
            rec = res.fetchone()
        return rec

    def fetchall(self, sql: str, params: tuple) -> List[Dict]:
        """Get all entries from db matching a query."""
        with self._get_auto_conn() as conn:
            res = conn.execute(sql, params)
            rec = res.fetchall()
        return rec
