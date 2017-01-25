#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Books - Serializers."""

# Models
from ..models.books import Category


def book_serializer(book):
    """Given a book object, return a python dictionary."""
    return {
        'title': book.title,
        'url': book.url,
        'thumbnail': book.thumbnail,
        'description': book.description,
        'pdf': book.pdf,
        'mobi': book.mobi,
        'epub': book.epub,
        'category': book.category.get().name,
        'subcategory': book.subcategory.get().name if book.subcategory else None,
    }
