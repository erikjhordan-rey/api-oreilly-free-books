#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Handlers - API module."""

from .base import APIHandler


class MenuHandler(APIHandler):
    """Menu Handler."""

    def get(self):
        """Return API available methods."""
        base_url = self.request.host_url + '{endpoint}'
        return self.reponse([
            {
                'name': 'API endpoints list',
                'allowed_methods': ['GET'],
                'url': base_url.format(endpoint='/')
            },
            {
                'name': 'Books list',
                'allowed_methods': ['GET'],
                'url': base_url.format(endpoint='/books')
            }
        ])
