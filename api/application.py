from flask import Flask
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
def getAllBooks():
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
def getBook(id):
    book = Book.query.get_or_404(id)
    result = {
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher

    }
    return result
