"""
This package contains all the api routes for the server
"""

from app import init_firebase

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

init_firebase()

from .api_urls import API_URL   # noqa
