import sqlite3
import sys
import csv
def printDB():
    # To retrieve data from a table use SELECT followed
    # by the items to retrieve and the table to
    # retrieve from
 
    try:
        result = theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")
 
        # You receive a list of lists that hold the result
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
 
    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")
 
    except:
        print("Couldn't Retrieve Data From Database")
 
# ---------- END OF FUNCTIONS ----------
 
# connect() will open an SQLite database, or if it
# doesn't exist it will create it
# The file appears in the same directory as this
# Python file
db_conn = sqlite3.connect('test.db')
 
print("Database Created")
 
# A cursor is used to traverse the records of a result
theCursor = db_conn.cursor()
 
# execute() executes a SQL command
# We organize our data in tables by defining their
# name and the data type for the data
 
# We define the table name
# A primary key is a unique value that differentiates
# each row of data in our table
# The primary key will auto increment each time we
# add a new Employee
# If a piece of data is marked as NOT NULL, that means
# it must have a value to be valid
 
# NULL is NULL and stands in for no value
# INTEGER is an integer
# TEXT is a string of variable length
# REAL is a float
# BLOB is used to store binary data
 
# You can delete a table if it exists like this
# db_conn.execute("DROP TABLE IF EXISTS Employees")
# db_conn.commit()
 
try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
 
    db_conn.commit()
 
    print("Table Created")
 
except sqlite3.OperationalError:
    print("Table couldn't be Created")
 
 
# To insert data into a table we use INSERT INTO
# followed by the table name and the item name
# and the data to assign to those items
 
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                "VALUES ('Gabriel', 'Felippe', 41, '123 Main St', '500,000', date('now'))")
 
db_conn.commit()
 
print("Employee Entered")
 
# Print out all the data in the database
printDB()
 
# Closes the database connection
db_conn.close()