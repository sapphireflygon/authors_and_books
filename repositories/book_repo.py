from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repo as author_repo


def save(book):
    sql = "INSERT INTO books (title, description, year_published, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.description, book.year_published, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def delete(id):
    sql = "DELETE FROM books WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        author = author_repo.select(result['author_id'])
        book = Book(result['title'], result['description'], result['year_published'], author, result['id'])
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], row['description'], row['year_published'], author, row['id'])
        books.append(book)
    return books


def update(book):
    sql = "UPDATE books SET (title, description, year_pubished, author_id) = (%s, %s, %s, %s) WHERE id=%s"
    values = [book.title, book.description, book.year_published, book.author.id, book.id]
    print(values)
    run_sql(sql, values)
