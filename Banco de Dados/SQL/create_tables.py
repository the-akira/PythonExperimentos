import sqlite3
from sqlite3 import Error
from create_con import create_connection

DB = 'sqlite.db'
conn = create_connection(DB)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_create_authors_table = """
CREATE TABLE IF NOT EXISTS authors(
    id integer PRIMARY KEY,
    name text NOT NULL,
    born_date text
);
"""

sql_create_books_table = """
CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author_id integer NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);
"""

if conn is not None:
    create_table(conn, sql_create_authors_table)
    create_table(conn, sql_create_books_table)
else:
    print('Error! Cannot create the database!')