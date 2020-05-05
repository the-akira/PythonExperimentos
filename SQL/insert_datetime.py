import sqlite3
from create_con import create_connection
import datetime
import random

DB = 'data.db'
conn = create_connection(DB)
cursor = conn.cursor()

class Task:
	def __init__(self, name, date):
		self.name = name 
		self.date = date
		self.priority = random.randrange(0,10)

def create_table():
	if conn:
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS tasks(
			name text NOT NULL,
			datestamp date,
			priority integer);"""
		)
	else:
		print('Error! Cannot create the database!')

def insert_data(task):
	data = (task.name, task.date, task.priority)
	cursor.execute("INSERT INTO tasks VALUES (?,?,?)", data)
	conn.commit()

def select_data():
	cursor.execute("SELECT * from tasks")
	rows = cursor.fetchall()

	for row in rows:
		print(row)

t1 = Task('Programar com Python', datetime.date(2020, 3, 4))
t2 = Task('Criar um Website', datetime.date(2020, 6, 7))
t3 = Task('Estudar C++', datetime.date(2021, 3, 2))
create_table()
insert_data(t1)
insert_data(t2)
insert_data(t3)
select_data()