__author__ = 'Ebenezer Adelwin Azumah'

import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from flask import request, jsonify
from functools import wraps
from utils.exceptions import JSONDataValidationError
from schema import DRAFT_7_SCHEMA, SCHEMA


def validate_json(f):
    """Validate json

    Arguments:

    """
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.get_json()
        except KeyError as e:
            raise JSONDataValidationError(message=str(
                e), payload={'path': 'expected %s' % e})
        except TypeError:
            raise JSONDataValidationError(message='Invalid Json Data', payload={
                'path': 'expected key `/data/`'})
        return f(*args, **kw)
    return wrapper


def validate_schema(schema_name):
    """Validate schema

    Arguments:
        schema_name {str} -- Registered schema name

    Keyword Arguments:
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.get_json(), SCHEMA[schema_name])
                return f(*args, **kw)
            except ValidationError as error:
                details = {
                    'path': '/%s' % (
                        '/'.join(
                            str(path) for path in list(error.absolute_path)[1::2])
                    )
                }
                raise JSONDataValidationError(
                    message=error.message, payload=details)
            except IndexError as error:
                details = {'path': ''}
                raise JSONDataValidationError(
                    message=error.message, payload=details)
        return wrapper
    return decorator
