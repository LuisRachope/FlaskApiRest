import sqlite3

from flask import g

# from src.main import ctx as app

DATABASE = "src/data/db_generic.db"


def get_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
