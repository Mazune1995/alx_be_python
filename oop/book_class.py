#!/usr/bin/python
# book_class.py

class Book:
    """A class that models a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor: Initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for debugging or reproduction."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
#
