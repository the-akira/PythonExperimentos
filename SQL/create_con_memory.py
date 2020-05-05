import sqlite3
from sqlite3 import Error

def create_connection():
    """ 
    create a database connection to a 
    database that resides in the memory
    """
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    conn = create_connection()
    print(conn)