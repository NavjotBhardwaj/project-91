import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Returns a DB connection
        For a db_file
    :param db_file: Database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def execute(conn, sql):
    """ Execute any given SQL
    :param conn: Connection object
    :param sql: Any valid SQL
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)
