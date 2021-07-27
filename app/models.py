from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship

from app import db

book2author = Table('book2author', db.metadata,
                          Column('book_id', ForeignKey('book.id')),
                          Column('author_id', ForeignKey('author.id'))
                          )


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=False)
    ISBN = db.Column(db.String(100), index=True, unique=True)
    authors = relationship("Author", secondary=book2author, back_populates="authors")

    def __str__(self):
        return f"<Ksiazka {self.name}>"


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=False)
    books = relationship("Book", secondary=book2author, back_populates="books")


class Rental(db.Model):
    __tablename__ = 'rental'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    status = db.Column(db.Integer, primary_key=False)

