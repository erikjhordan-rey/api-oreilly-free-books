#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Books - API module."""

# Handlers
from .base import APIHandler

# Models
from ..models.books import Book

# Serializers
from .serializers import book_serializer


class BooksListHandler(APIHandler):
    """Books list Handler."""

    def get(self):
        """Return a list with all books."""
        q = Book.query()
        books = [book_serializer(b) for b in q]
        return self.reponse(books)
