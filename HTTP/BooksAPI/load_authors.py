from app import db, Author
import csv

authors = []

with open('data/authors.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        authors.append(row[0])

for author in authors:
    author = Author(name=author)
    db.session.add(author)
    db.session.commit()