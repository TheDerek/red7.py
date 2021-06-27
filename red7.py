#!/usr/bin/env python3.9

import sqlite3
import datetime

from thederek.red7 import game

def create_database(schema: str):
    conn = sqlite3.connect(":memory:")
    conn.executescript(schema)
    conn.commit()
    return conn


def copy_database(source_connection, dest_dbname=":memory:"):
    """Return a connection to a new copy of an existing database.
    Raises an sqlite3.OperationalError if the destination already exists.
    """
    script = "".join(source_connection.iterdump())
    dest_conn = sqlite3.connect(dest_dbname)
    dest_conn.executescript(script)
    return dest_conn

if __name__ == "__main__":
    conn = create_database(open("red7.sql").read())

    game = game.Game(4).create(conn)
    copy_database(conn, f"logs/{datetime.datetime.now().isoformat()}.db")
    game.play("r6")

    print(game.id)
    #copy_database(conn, f"logs/{datetime.datetime.now().isoformat()}.db")
