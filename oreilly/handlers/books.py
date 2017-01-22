#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Books - API module."""

# Handlers
from .base import APIHandler

# Models
from ..models.books import (
    Book,
    Category
)


class BooksListHandler(APIHandler):
    """Menu Handler."""

    def get(self):
        """Return API available methods."""
        return self.reponse({'status': 'ok'})
