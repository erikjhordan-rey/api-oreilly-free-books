#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Cron jobs routes module."""

# WebApp 2
from webapp2_extras.routes import RedirectRoute

# Handlers
from . import handlers


_routes = [

    RedirectRoute(
        template='/jobs/retrieve_books',
        handler=handlers.RetrieveBooksHandler,
        name='jobs__retrieve_books',
        strict_slash=True
    ),

]


def get_routes():
    """Return routes."""
    return _routes


def add_routes(app):
    """Add routes to app."""
    for r in _routes:
        app.router.add(r)
