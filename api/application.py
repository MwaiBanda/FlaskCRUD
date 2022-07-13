from flask import Flask, request
from .shared.db import db
from .data.Book import Book

app = Flask(__name__)

"""
Book Model
id
book_name
author
publisher
"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


@app.route('/')
def home():
    return "Hello World"


@app.route('/books')
def get_all_books():
    books = Book.query.all()
    result = []
    for book in books:
        book = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        result.append(book)

    return {'books': result}


@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    result = {
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher

    }
    return result


@app.route('/books', methods=['POST'])
def add_book():
    book = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher']
    )
    db.session.add(book)
    db.session.commit()
    return {"success": f"message: Added book with ID: {book.id}"}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": f"message: Book with ID: {id} not found"}
    db.session.delete(book)
    db.session.commit()
    return {"success": f"message: Book with ID: {id} deleted"}


@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": f"message: Book with ID: {id} not found"}
    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']
    db.session.commit()
    return {"success": f"message: Book with ID: {id} updated"}
