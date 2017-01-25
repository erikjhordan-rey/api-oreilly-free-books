#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Handlers - Base module."""

# WebApp 2
from webapp2 import RequestHandler

# Utilities
import json


class APIHandler(RequestHandler):
    """API Handler.

    Setup request and reponse objects.
    """

    def reponse(self, data):
        """Set Content-Type and JSON content."""
        response = self.response
        response.headers['Content-Type'] = 'application/json'
        json.dump(data, response.out)
        return response
