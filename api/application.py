from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
Book Model
id
book_name
author
publisher
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True)
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.book_name} by {self.author}'


@app.route('/')
def home():
    return "Hello World"


@app.route('/books')
def getBooks():
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
def getbook(id):
    book = Book.query.get_or_404(id)
    result = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher

    }
    return result