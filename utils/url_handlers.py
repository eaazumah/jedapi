__author__ = 'Ebenezer Adelwin Azumah'

from typing import Callable, Dict, List

from flask import Flask
from flask_restful import Resource, Api


def add_api_resource(resource: Resource, url: str, endpoint: str, api: Api) -> None:
    url = tuple(['/api/%s' % route for route in url]) if isinstance(url,
                                                                    tuple) else ('/api/%s' % url, )
    api.add_resource(resource, *url, endpoint=endpoint)


def register_apis(api_urls: Dict, api: Api) -> None:
    """Registers all routes from Restful

    Arguments:
            api_urls {List[dict]} -- List of all routes: refer to urls.py
            api {Api} -- Restful Api class
    """

    for api_url in api_urls:
        add_api_resource(api_url.get('resource'), api_url.get(
            'url'), api_url.get('endpoint'), api)
