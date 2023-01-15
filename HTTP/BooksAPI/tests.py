from app import db, app, Author, Book
from dotenv import load_dotenv
from flask import Flask
import unittest
import json
import os

class TestAuthors(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

    def test_add_author(self):
        response = self.client.post(
            '/authors', 
            data=json.dumps({'name': 'Author1'}), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.data)['name'], 
            'Author1'
        )

    def test_get_authors(self):
        response = self.client.get('/authors')
        self.assertEqual(response.status_code, 200)

    def test_get_author_by_id(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        response = self.client.get(f'/authors/{author.id}')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['id'], author.id)
        self.assertEqual(response_data['name'], author.name)

    def test_get_author_by_invalid_id(self):
        response = self.client.get('/authors/999')
        self.assertEqual(response.status_code, 404)

    def test_update_author_with_valid_data(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        data = {'name': 'Author2'}
        response = self.client.put(
            f'/authors/{author.id}', 
            data=json.dumps(data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['name'], 'Author2')

    def test_update_author_with_no_data(self):
        author = Author(name='Author1')
        response = self.client.put(f'/authors/{author.id}')
        self.assertEqual(response.status_code, 404)

    def test_update_author_with_no_id(self):
        data = {'name': 'Author2'}
        response = self.client.put(
            '/authors/', 
            data=json.dumps(data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_author_by_id(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()

        response = self.client.delete(f'/authors/{author.id}')
        self.assertEqual(response.status_code, 200)

        author = Author.query.get(author.id)
        self.assertIsNone(author)

    def test_delete_author_by_invalid_id(self):
        response = self.client.delete('/authors/999')
        self.assertEqual(response.status_code, 404)

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

    def test_add_book(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        response = self.client.post(
            '/books', 
            data=json.dumps({
                'title': 'Book1', 
                'genre': 'Fiction', 
                'author_id': author.id
            }), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.data)['title'], 
            'Book1'
        )

    def test_get_books(self):
        author = Author(name='Author2')
        db.session.add(author)
        db.session.commit()
        book = Book(title='Book2', genre='Fiction', author=author)
        db.session.add(book)
        db.session.commit()
        response = self.client.get(f'/book')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)[0]['title'], 'Book2')

    def test_get_book(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        book = Book(title='Book1', genre='Fiction', author=author)
        db.session.add(book)
        db.session.commit()
        response = self.client.get(f'/book/{book.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['title'], 'Book1')

    def test_update_book(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        book = Book(title='Book1', genre='Fiction', author=author)
        db.session.add(book)
        db.session.commit()
        response = self.client.put(
            f'/books/{book.id}', 
            data=json.dumps({'title': 'Book2'}), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['title'], 'Book2')

    def test_update_book_with_invalid_author_id(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        book = Book(title='Book1', genre='Fiction', author=author)
        db.session.add(book)
        db.session.commit()
        response = self.client.put(
            f'/books/{book.id}', 
            data=json.dumps({
                'title': 'New Title', 
                'genre': 'New Genre', 
                'author_id': 999
            }), 
            content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_update_book_with_no_data(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        book = Book(title='Book1', genre='Fiction', author=author)
        db.session.add(book)
        db.session.commit()
        response = self.client.put(f'/books/{book.id}')
        self.assertEqual(response.status_code, 400)

    def test_update_book_with_no_id(self):
        author = Author(name='Author1')
        response = self.client.put(
            '/books/', 
            data=json.dumps({
                'title': 'New Title', 
                'genre': 'New Genre', 
                'author_id': author.id
            }), 
            content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_add_book_with_no_data(self):
        response = self.client.post('/books')
        self.assertEqual(response.status_code, 400)

    def test_add_book_with_invalid_author_id(self):
        data = {
            'title': 'Book1',
            'genre': 'Genre1',
            'author_id': 999
        }
        response = self.client.post(
            '/books', 
            data=json.dumps(data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_add_book_with_valid_data(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()

        data = {
            'title': 'Book1',
            'genre': 'Genre1',
            'author_id': author.id
        }

        response = self.client.post(
            '/books', 
            data=json.dumps(data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertEqual(response_data['title'], data['title'])
        self.assertEqual(response_data['genre'], data['genre'])
        self.assertEqual(response_data['author']['id'], data['author_id'])

    def test_delete_book_by_id(self):
        author = Author(name='Author1')
        book = Book(title='Book1', genre='Fiction', author=author)
        db.session.add(author)
        db.session.commit()

        response = self.client.delete(f'/books/{book.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_books_by_author_id(self):
        author = Author(name='Author1')
        db.session.add(author)
        db.session.commit()
        book1 = Book(title='Book1', genre='Fiction', author=author)
        book2 = Book(title='Book2', genre='Non-Fiction', author=author)
        db.session.add(book1)
        db.session.add(book2)
        db.session.commit()

        response = self.client.get(f'/book/author/{author.id}')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIsInstance(response_data, list)
        self.assertEqual(len(response_data), 2)
        self.assertEqual(response_data[0]['title'], 'Book1')
        self.assertEqual(response_data[0]['genre'], 'Fiction')
        self.assertEqual(response_data[1]['title'], 'Book2')
        self.assertEqual(response_data[1]['genre'], 'Non-Fiction')

testing = (os.getenv('TESTING', 'False') == 'True')

if __name__ == '__main__' and testing:
    unittest.main()
else:
    print('TESTING DISABLED')