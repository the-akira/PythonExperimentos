import sqlite3
from sqlite3 import Error
from create_con import create_connection

DB = 'sqlite.db'
conn = create_connection(DB)

def create_author(conn, author):
	sql = """INSERT INTO authors(name,born_date)
		VALUES(?,?)"""
	cur = conn.cursor()
	try:
		with conn:
			cur.execute(sql, author)
	except sqlite3.IntegrityError:
		print("couldn't add author")
	return cur.lastrowid

def create_books(conn, books):
	sql = """INSERT INTO books(title,author_id)
		VALUES(:title,:author_id)"""
	cur = conn.cursor()
	try:
		with conn:
			cur.executemany(sql, books)
	except sqlite3.IntegrityError:
		print("couldn't add books")
	return cur.lastrowid

with conn:
	author = ('Aldous Huxley', '1894-07-26')
	author_id = create_author(conn, author)

	books = [
		('Brave New World', author_id),
		('The Perennial Philosophy', author_id),
		('The Doors of Perception', author_id),
		('The Art of Seeing', author_id),
		('Update Field', 5)
	]

	create_books(conn, books)