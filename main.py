__author__ = 'Ebenezer Adelwin Azumah'

from typing import Dict

from flask import json, render_template, jsonify
from werkzeug.exceptions import HTTPException
from utils.url_handlers import register_apis
from utils.exceptions import BaseError
from flask_restful import Api
from app import create_app
from urls import API_URL

app = create_app()
api = Api(app)
register_apis(API_URL, api)


@app.errorhandler(BaseError)
def handle_errors(error: BaseError) -> Dict:
    """handler to serialize exceptions to json response
    """
    response = jsonify({'error': error.to_dict()})
    response.status_code = error.error_code
    return response


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    # now you're handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods',
                         'POST, GET, OPTIONS, DELETE')
    response.headers.add('Access-Control-Allow-Headers',
                         'content-type, Authorization')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
