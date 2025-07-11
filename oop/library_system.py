#!/usr/bin/python
# library_system.py

class Book:
    """Base class for all books."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Represents a digital book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Represents a physical book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Composition: Manages a collection of books."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        for book in self.books:
            print(book.get_info())
#
