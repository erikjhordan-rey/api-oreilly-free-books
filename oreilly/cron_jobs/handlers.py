#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Cron Jobs module."""

# Google App Engine
from google.appengine.ext import ndb

# Handlers
from ..handlers.base import APIHandler

# Models
from ..models.books import Category, Book

# Utilities
from lxml import html
import urllib2


class RetrieveBooksHandler(APIHandler):
    """Menu Handler."""

    source_url = 'http://www.oreilly.com/programming/free/'

    def append_book(self, book, category, subcategory=None):
        """Add book to datastore."""
        # Get properties by attribute value.
        title = book.get('title', '')
        url = book.get('href', '').split('?')[0]
        description = book.get('data-content', '')
        thumbnail = book.xpath('.//img')[0].get('src', '')

        # NOQA: If URL ends with .csp, will replace it for the corresponding extension.
        if url.endswith('.csp'):
            pdf = url.replace('.csp', '.pdf')
            epub = url.replace('.csp', '.epub')
            mobi = url.replace('.csp', '.mobi')
        # Else, will set to None
        else:
            pdf = None
            epub = None
            mobi = None

        # Create Book entity.
        book = Book(
            title=title,
            url=url,
            description=description,
            category=category.key,
            thumbnail=thumbnail,
            pdf=pdf,
            epub=epub,
            mobi=mobi,
        )
        if subcategory:
            book.subcategory = subcategory.key
        book.put()

    def get(self):
        """Return API available methods."""
        # Remove old data
        cs = Category.query()
        ndb.delete_multi([x.key for x in cs])
        bs = Book.query()
        ndb.delete_multi([x.key for x in bs])

        # Count variables
        categories_count = 0
        subcategories_count = 0
        books_count = 0

        # NOQA: lxml tree from web page response and search for category boxes.
        tree = html.fromstring(urllib2.urlopen(self.source_url).read())
        category_boxes = tree.xpath('//div[@class="callout-row"]')

        for category_box in category_boxes:

            # Get box title by filtering all H3 tags without attributes.
            category_name = category_box.xpath('.//h3[not(@*)]/text()')[0]

            # Create category entity and update counters.
            category = Category(name=category_name, category=True, subcategory=False)  # NOQA
            category.put()
            categories_count += 1

            # Get subcategories by looking for all divs with the right class.
            subcategories = category_box.xpath('.//div[not(@class="product-row cover-showcase")]')  # NOQA
            book_expression = './/a'

            # If categories, iterate each and append book with subcategory
            for subcategory_box in subcategories:
                # Ger subcategory title by filtering the first H3 tag.
                subcategory_name = subcategory_box.xpath('.//h3/text()')[0]

                # Create category entity and update counters.
                subcategory = Category(name=subcategory_name, category=False, subcategory=True)  # NOQA
                subcategory.put()
                subcategories_count += 1

                books = subcategory_box.xpath(book_expression)
                for book in books:
                    self.append_book(book, category, subcategory)
                    books_count += 1

            # Else, get books and append each with category only
            if not subcategories:
                books = category_box.xpath(book_expression)
                for book in books:
                    self.append_book(book, category)
                    books_count += 1

        return self.reponse({
            'status': 'ok',
            'books_added': books_count,
            'categories_added': categories_count,
            'subcategories_added': subcategories_count,
        })
