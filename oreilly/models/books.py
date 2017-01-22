#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Models - Books."""

# App Engine Extensions
from google.appengine.ext import ndb, db


class Category(ndb.Model):
    """Category/Subcategory model class."""

    name = ndb.StringProperty()
    category = ndb.BooleanProperty(default=False)
    subcategory = ndb.BooleanProperty(default=False)


class Book(ndb.Model):
    """Book reference model class."""

    category = ndb.KeyProperty(kind=Category)
    subcategory = ndb.KeyProperty(kind=Category)

    title = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)

    thumbnail = ndb.StringProperty()
    description = ndb.StringProperty()

    # Download URLs
    pdf = ndb.StringProperty()
    mobi = ndb.StringProperty()
    epub = ndb.StringProperty()
