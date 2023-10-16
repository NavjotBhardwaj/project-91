from top_scorer_db.db_setup import db_lib as db
import csv
import logging
logger = logging.getLogger(__name__)

from os.path import dirname, abspath

ROOT_DIR = dirname(dirname(abspath(__file__)))
database = ROOT_DIR + "/db/top_scorer.db"

def create_tables():
    """
    Creates the table if it doesn't exist
    In-real world this will be one-time deployed data model staging table
    """  
    sql_create_students_stg_table = """ CREATE TABLE IF NOT EXISTS stg_students (
                                        f_name text NOT NULL,
                                        s_name text,
                                        score text NOT NULL
                                    ); """

    sql_create_students_cln_table = """ CREATE TABLE IF NOT EXISTS cln_students (
                                        f_name text NOT NULL,
                                        s_name text,
                                        score int NOT NULL
                                    ); """                                    

    # Get a database connection
    conn = db.create_connection(database)

    logger.info("Creating the tables if they do not exist.")
    # Create table
    if conn is not None:
        # Create students table
        #db.execute(conn, "DROP TABLE stg_students")
        #db.execute(conn, "DROP TABLE cln_students")
        db.execute(conn, sql_create_students_stg_table)
        db.execute(conn, sql_create_students_cln_table)
    else:
        logger.error("Error! cannot create the database connection.")

def load_to_stg(file_path: str, has_header: bool):
    """
    Loading data as text into local DB
    Staging the data as text cols
    """
    # Get a database connection
    conn = db.create_connection(database)
    logger.info("Loading to stage table")
    with open('/Users/navjotbhardwaj/Desktop/91/project-91/testdata/test_data.csv','r') as f:
        dr = csv.DictReader(f) # comma is default delimiter
        data = []
        for line in f:
            # Removing newline since we are doing string processing
            line = line.rstrip()
            # Checking for header and skipping it in case it exists
            if has_header:
                has_header = False
                continue
            (f_name, l_name, marks) = line.split(',')
            data.append((f_name, l_name, marks))
        #print(data)
        to_db = [(i[0], i[1], i[2]) for i in data]
        conn.execute("DELETE FROM stg_students where 1=1;")
        conn.executemany("INSERT INTO stg_students (f_name, s_name, score) VALUES (?, ?, ?);", to_db)
        conn.commit()
        logger.info("Stage load is completed")
        
def load_to_main():
    """
    Loading data to main table with transformation
    In real world here we will apply
    - Load strategies
    - Transformation
    - This will be embedded in DBT or ADF etc.
    """
    logger.info("Loading to main table")              
    # Get a database connection
    conn = db.create_connection(database)
    conn.execute("DELETE FROM cln_students where 1=1;")
    conn.execute("""INSERT INTO cln_students
                        SELECT f_name, s_name,
                        CAST (SCORE AS INT)
                        FROM stg_students                
                 ;""")
    conn.commit()
    logger.info("Loading to main table done.")
    
def project_91_calculation():
    """
    Finding the highest score and printing the results as requested
    """
    # Get a database connection
    conn = db.create_connection(database)
    cur = conn.cursor()
    cur.execute("""SELECT f_name, s_name, score FROM(
                    SELECT 
                    f_name, 
                    s_name, 
                    score,
                    RANK() over (order by score DESC) rnk
                    FROM cln_students) sub_table
                    where rnk = 1
                    """)
    rows = cur.fetchall()
    
    print('\n'.join(' '.join(map(str, row[0:2])) for row in rows) + 
        "\nScore: " + str(rows[1][2]))
    return rows