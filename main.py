#!/usr/bin/python
# -*- coding: utf-8 -*-

u"""O’Reilly's Free Books API.

REST API that exposing scrapped data from O’Reilly's
Free Books website (http://www.oreilly.com/programming/free/).
"""

# Python libraries
import os
import sys

# Third party libraries
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'oreilly'))

# WebApp 2
import webapp2

# Routes
from config import routes

# App initialization.
app = webapp2.WSGIApplication(debug=os.environ.get('DEBUG', 'prod') == 'dev')

routes.add_routes(app)
