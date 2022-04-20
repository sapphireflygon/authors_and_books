from flask import Flask, redirect, render_template, request, Blueprint
from repositories import author_repo, book_repo
from models.author import Author
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/')
def books():
    books = book_repo.select_all()
    return render_template("/index.html", all_books = books)


@books_blueprint.route('/books')
def all_books():
    books = book_repo.select_all()
    return render_template("books/books.html", all_books = books)


@books_blueprint.route('/books/newbook', methods=["POST"])
def add_book():
    title = request.form['title']
    description = request.form['description']
    author_id = request.form['author_id']
    year_published = request.form['year_published']
    author = author_repo.select(author_id)
    book = Book(title, description, year_published, author)
    book_repo.save(book)
    return redirect('/books')


@books_blueprint.route('/books/new')
def new_book():
    authors = author_repo.select_all()
    print(authors)
    return render_template('/books/new_book.html', all_authors=authors)


@books_blueprint.route('/books/<id>', methods=["GET"])
def show_one_book(id):
    book = book_repo.select(id)
    return render_template('/books/show.html', book=book)


@books_blueprint.route('/books/<id>/edit', methods=["GET"])
def edit_book(id):
    book=book_repo.select(id)
    authors=author_repo.select_all()
    print(book)
    print(authors)
    return render_template("/books/edit.html", book=book, all_authors=authors)


@books_blueprint.route('/books/<id>', methods=["POST"])
def update_book(id):
    title = request.form['title']
    description = request.form['description']
    author_id = request.form['author_id']
    year_published = request.form['year_published']
    author = author_repo.select(author_id)
    book = Book(title, description, year_published, author, id)
    book_repo.update(book)
    return redirect('/books')