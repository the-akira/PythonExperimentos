import sqlite3
from sqlite3 import Error
from create_con import create_connection

DB = 'sqlite.db'
conn = create_connection(DB)

def select_book(conn, id):
    cur = conn.cursor()
    cur.execute('SELECT * from books WHERE id=:id', {'id':id})

    row = cur.fetchone()
    print(row)

def select_books(conn):
    cur = conn.cursor()
    cur.execute('SELECT * from books')

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_author(conn, id):
    cur = conn.cursor()
    cur.execute('SELECT * from authors WHERE id=?', (id,))

    row = cur.fetchone()
    print(row)

def select_authors(conn):
    cur = conn.cursor()
    cur.execute('SELECT * from authors')

    rows = cur.fetchall()
    for row in rows:
        print(row)

with conn:
    print('SELECT * from books;')
    select_books(conn)
    print('SELECT * from authors;')
    select_authors(conn)
    print('SELECT * from books where id = 3;')
    select_book(conn, 3)
    print('SELECT * from authors where id = 1;')
    select_author(conn, 1)