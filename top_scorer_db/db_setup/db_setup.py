import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ 
    create a database connection to a SQLite database 
    One time requirement
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"/Users/navjotbhardwaj/Desktop/91/project-91/db/top_scorer.db")