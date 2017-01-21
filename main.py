# Copyright 2017 Erik Jhordan Rey.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
sys.path.insert(0, 'libs')
import logging
import json as simplejson
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch
import webapp2

class MainHandler(webapp2.RequestHandler):

    global OREILLY_FREE_BOOKS_URL
    OREILLY_FREE_BOOKS_URL = "http://www.oreilly.com/programming/free/"
    global OREILLY_FREE_BOOKS_PAGE
    OREILLY_FREE_BOOKS_PAGE = urlfetch.fetch(OREILLY_FREE_BOOKS_URL, deadline=90).content
    global OREILLY_FREE_BOOKS_SECTIONS_SIZE
    OREILLY_FREE_BOOKS_SECTIONS_SIZE = 2

    def get(self):

        oreilly_page = BeautifulSoup(OREILLY_FREE_BOOKS_PAGE)

        oreilly_json = []
        sub_category_json = []
        books_download_json = []
        books_json = []

        divs_book_section = oreilly_page.findAll("div", {"class":"callout-row"});

        for sections, div_book_section in enumerate(divs_book_section):

            if sections <= OREILLY_FREE_BOOKS_SECTIONS_SIZE:

                category = div_book_section.find("h3")

                if not div_book_section.has_attr("style"):

                    sub_book_section = div_book_section.findAll("div", style="margin:0 auto;")
                    sub_book_section += div_book_section.findAll("div", style="max-width:760px; margin:0 auto;")

                    for sub_category in sub_book_section:

                        sub_category_title = sub_category.find("h3").text
                        books = sub_category.findAll("a")

                        for book in books:
                            create_book = Book(book)
                            book_json = create_book.book_to_book_json_mapper()
                            books_json.append(book_json)
                            book_json = []

                        sub_category_json.append({"sub_category": sub_category_title, "books": books_json})
                        books_json = []

                    oreilly_json.append({"category": category.text, "sub_categories": sub_category_json })

                else:
                    
                    books = div_book_section.findAll("a")
                    for book in books:
                        create_book = Book(book)
                        book_json = create_book.book_to_book_json_mapper()
                        books_json.append(book_json)
                        book_json = []

                    oreilly_json.append({"category": category.text, "books": books_json})
                    books_json = []

        self.response.write(simplejson.dumps(oreilly_json))
        self.response.headers['Content-Type'] = 'application/json'

class Book(object):

    def __init__(self, book):
        self.book = book

    def book_to_book_json_mapper(self):

        book_json = {}
        book_json['title'] = self.book.find('img')['alt']
        book_json['description'] = self.book.get('data-content')
        book_json['thumbnail'] = self.book.find('img')['src']
        href = self.book.get('href')
        book_json['href'] = href
        download_json = Download(href).href_to_download_json_mapper()
        if download_json:
           book_json['download'] = download_json

        return book_json



class Download(object):

    def __init__(self, href):
        self.href = href

    def href_to_download_json_mapper(self):
        HREF_START = "http://www.oreilly.com/programming/free/"
        HREF_END = ".csp"
        OREILLY_BUCKET_PROGRAMMING = "http://www.oreilly.com/programming/free/files/"
        EXTENSION_EPUB = ".epub"
        EXTENSION_MOBI = ".mobi"
        EXTENSION_PDF = ".pdf"
        books_download_json = []

        if HREF_START in self.href:
           book_href_title = (self.href.split(HREF_START))[1].split(HREF_END)[0]
           book_epub = OREILLY_BUCKET_PROGRAMMING + book_href_title + EXTENSION_EPUB
           book_mobi = OREILLY_BUCKET_PROGRAMMING + book_href_title + EXTENSION_MOBI
           book_pdf = OREILLY_BUCKET_PROGRAMMING + book_href_title + EXTENSION_PDF
           books_download_json.append({"epub": book_epub, "mobi": book_mobi , "pdf": book_pdf })


        return books_download_json


app = webapp2.WSGIApplication([
    ('/oreilly-free', MainHandler)
], debug=True)
