from re import L


class Book:
    def __init__(self, input_title, input_description, input_year_published, author, id=None):
        self.title = input_title
        self.description = input_description
        self.year_published = input_year_published
        self.id = id
        self.author = author