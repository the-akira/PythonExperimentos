import sqlite3
from sqlite3 import Error
from create_con import create_connection

DB = 'sqlite.db'
conn = create_connection(DB)

def update_book(conn, book):
	sql = """UPDATE books SET
				title = ?,
				author_id = ?
			WHERE id = ?"""
	cur = conn.cursor()
	cur.execute(sql, book)
	conn.commit()

book = ('Ape and Essence', 1, 5)

with conn:
	update_book(conn,book)