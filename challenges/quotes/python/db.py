# coding: utf-8
"""Module database to store team score."""
import logging
import sqlite3
from datetime import datetime
from pathlib import Path

from utils.sqlite import SqliteDb


class DashboardDb(SqliteDb):
    """Wrap SQLite db to store dashboard info."""

    def __init__(self, db_path: Path):
        """Initialize."""
        sql = """
        PRAGMA foreign_keys = ON;
        CREATE TABLE
            teams(
                id_team INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
        );
        CREATE TABLE
            scores(
                id_score INTEGER PRIMARY KEY AUTOINCREMENT,
                date_inserted TIMESTAMP,
                id_team INTEGER,
                file_name TEXT,
                run_info TEXT,
                f REAL,
                r REAL,
                p REAL,
                score_dump TEXT,
                FOREIGN KEY(id_team) REFERENCES team(id_team)
        );
        INSERT INTO teams(name) VALUES ("Elis*");
        INSERT INTO teams(name) VALUES ("ciTAL");
        INSERT INTO teams(name) VALUES ("HackaTeam");
        INSERT INTO teams(name) VALUES ("FlowBERT");
        INSERT INTO teams(name) VALUES ("Team 5");
        INSERT INTO teams(name) VALUES ("Team 6");
        """
        super().__init__(db_path, sql)

    def put(
        self,
        date_inserted: datetime,
        id_team: int,
        file_name: str,
        run_info: str,
        f: float,
        r: float,
        p: float,
        score_dump: str,
    ):
        """Insert a score into the db."""
        with self._get_auto_conn() as conn:
            try:
                conn.execute(
                    """
                    INSERT INTO scores(date_inserted, id_team, file_name, run_info, f, r, p, score_dump)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                    ;
                    """,
                    (
                        date_inserted,
                        id_team,
                        file_name,
                        run_info,
                        f,
                        r,
                        p,
                        score_dump,
                    ),
                )
            except sqlite3.Error as error:
                logging.warning("Db error : %s", error)

    def get_all(self):
        """Get all scores."""
        sql = """
            SELECT date_inserted, name, file_name, run_info, f, r, p, score_dump
            FROM scores
            INNER JOIN teams
            ON scores.id_team = teams.id_team
            ORDER by date_inserted DESC
            ;
            """
        with self._get_auto_conn() as conn:
            res = conn.execute(sql)
            rec = res.fetchall()
        return rec

    def get_leader(self):
        """Get best scores per team."""
        sql = """
            SELECT
                name,
                MAX(f)
            FROM scores
            INNER JOIN teams
            ON scores.id_team = teams.id_team
            GROUP BY name
            ORDER BY 2 DESC
        ;"""
        res = self.fetchall(sql, ())

        return res

    def get_teams_mapping(self):
        """Return mapping between team name and id."""
        sql = """
            SELECT id_team, name
            FROM teams;
        """
        res = self.fetchall(sql, ())

        return [(t["name"], t["id_team"]) for t in res]
