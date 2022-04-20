# aka console.py

import pdb
from models.author import Author
from models.book import Book

import repositories.author_repo as author_repo
import repositories.book_repo as book_repo

author1 = Author("William", "Shakespeare")
author_repo.save(author1)

author2 = Author("Stephen", "King")
author_repo.save(author2)

book1 = Book("Macbeth", "The Scottish play", 1623, author1)
book_repo.save(book1)

book2 = Book("It", "Spooky clown dude wreaks havoc", 1986, author2)
book_repo.save(book2)


book_repo.select(book2.id)
author_repo.select(author1.id)

# book_repo.delete(book2.id)
# author_repo.delete(author2.id)
