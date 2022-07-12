from ..shared.db import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True)
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.book_name} by {self.author}'
