__author__ = 'Ebenezer Adelwin Azumah'

"""
Register all routes from flask restful Resource
eg.
1. API_URL = [
    {
        'resource': TestResource,
        'url': 'test',
        'endpoint': 'test'
    },
]
"""

from resources.test_resource import TestResource
from resources.user_resource import UserResource


API_URL = [
    {
        'resource': TestResource,
        'url': 'test',
        'endpoint': 'test'
    },
    {
        'resource': UserResource,
        'url': ('user', 'user/<string:id>'),
        'endpoint': 'user'
    },

]
