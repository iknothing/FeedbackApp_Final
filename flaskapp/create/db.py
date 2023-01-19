import sqlite3
import os

def create_db():
    basedir = os.path.abspath(os.path.dirname(__file__))
    DBFILE = "user.db"
    SQLFILE = "dbcreate.sql"
    # (D) IMPORT SQL
    try:
        conn = sqlite3.connect(DBFILE)
        with open(SQLFILE) as f:
            conn.executescript(f.read())
        conn.commit()
    except:
        print("Error in creating database")
    conn.close()
create_db()