#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Main routes module."""

# WebApp 2
from webapp2_extras.routes import RedirectRoute

secure_scheme = 'https'

from oreilly.handlers import api as api_handlers
from oreilly.handlers import books as books_handlers

_routes = [

    RedirectRoute(
        template='/',
        handler=api_handlers.MenuHandler,
        name='menu',
        strict_slash=True
    ),

    RedirectRoute(
        template='/books',
        handler=books_handlers.BooksListHandler,
        name='books_list',
        strict_slash=True
    ),

]


def get_routes():
    """Return routes."""
    return _routes

def add_routes(app):
    """Add routes to app."""
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
