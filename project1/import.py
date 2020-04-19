import os, csv
from flask import Flask, session, render_template, request, redirect,url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
db = db_session()

app1 = Flask(__name__)
app1.config["SESSION_PERMANENT"] = False
app1.config["SESSION_TYPE"] = "filesystem"
Session(app1)
db1= SQLAlchemy()
app1.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app1.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app1.app_context().push()


db1.init_app(app1)

class Book(db1.Model):
	__tablename__ = "books"
	isbn = db.Column(db.String, primary_key = True)
	title = db.Column(db.String, nullable = False)
	author = db.Column(db.String, nullable = False)
	year = db.Column(db.String, nullable = False)

	def __init__(self, isbn, title, author, year):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.year = year

def main():

    b = open("books.csv")
    books = csv.reader(b)
    i = 0
    for ISBN, title, author, year in books:
        if i != 0:
            book = Book(isbn=ISBN, title=title, author=author, year=year)
            print(book.title)
            db1.session.add(book)
        i += 1
    db1.commit()
    db1.close()

if __name__ == "__main__":
    main()