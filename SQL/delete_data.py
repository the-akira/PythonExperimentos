import sqlite3
from sqlite3 import Error
from create_con import create_connection

DB = 'sqlite.db'
conn = create_connection(DB)

def delete_book(conn, id):
	sql = f'DELETE FROM books where id = {id}'
	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()

def delete_all_authors(conn):
	sql = 'DELETE FROM authors'
	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()

with conn:
	delete_book(conn, 5)
	delete_all_authors(conn)