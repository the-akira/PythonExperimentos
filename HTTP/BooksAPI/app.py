from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
testing = (os.getenv('TESTING', 'False') == 'True')

if testing:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate()
migrate.init_app(app, db)

app.app_context().push()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", backref="author", lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'genre')
    author = ma.Nested(AuthorSchema)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

@app.route('/', methods=['GET'])
def home():
    return {
        "API":"Books and Authors",
        "Creator": "ChatGPT"
    }

@app.route('/authors', methods=['POST'])
def add_author():
    data = request.get_json()
    author = Author(name=data["name"])
    db.session.add(author)
    db.session.commit()
    return author_schema.jsonify(author)

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return authors_schema.jsonify(authors)

@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get_or_404(author_id)
    return author_schema.jsonify(author)

@app.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    data = request.get_json()
    author.name = data["name"]
    db.session.commit()
    return author_schema.jsonify(author)

@app.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return author_schema.jsonify(author)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    author = Author.query.get_or_404(data["author_id"])
    book = Book(title=data["title"], genre=data["genre"], author=author)
    db.session.add(book)
    db.session.commit()
    return book_schema.jsonify(book)

@app.route('/book', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)

@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return book_schema.jsonify(book)

@app.route('/book/author/<author_id>', methods=['GET'])
def get_book_by_author_id(author_id):
    author = Author.query.get_or_404(author_id)
    books = Book.query.filter_by(author=author)
    return jsonify([{'title':book.title,'genre':book.genre} for book in books])

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)
    if "title" in data:
        book.title = data["title"]
    if "author_id" in data:
        author = Author.query.get_or_404(data["author_id"])
        book.author = author
    if "genre" in data:
        book.genre = data["genre"]
    db.session.commit()
    return book_schema.jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book:
        db.session.delete(book.author)
        db.session.delete(book)
        db.session.commit()
        return book_schema.jsonify(book)
    else:
        return "Book not found", 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)