from app import db, Book, Author
import csv

books = []

with open('data/books.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        books.append(row)

for book in books:
    author = Author.query.get_or_404(int(book["author"]))
    book = Book(title=book["title"], genre=book["genre"], author_id=author.id)
    db.session.add(book)
    db.session.commit()