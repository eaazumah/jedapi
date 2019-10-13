"""This package contains the schema structure of a requests and response
for making sure clients send the right requests and server sends the right response
This makes testing and debugging easier
"""

DRAFT_7_SCHEMA = 'http://json-schema.org/draft-07/schema#'
NULL_SCHEMA = {'type': 'null'}
STRING_SCHEMA = {'type': 'string'}
STRING_ARRAY_SCHEMA = {"type": "array", "items": {"type": "string"}}
BOOLEAN_SCHEMA = {'type': 'boolean'}
INTEGER_SCHEMA = {'type': 'integer'}
FLOAT_SCHEMA = {'type': 'number'}
TIMESTAMP_SCHEMA = {'type': 'integer', 'minInclusive': 0}
NULLABLE_STRING_SCHEMA = {'anyOf': [STRING_SCHEMA, NULL_SCHEMA]}
NULLABLE_INTEGER_SCHEMA = {'anyOf': [INTEGER_SCHEMA, NULL_SCHEMA]}
EMAIL_SCHEMA = {
    'format': 'email'
}
NULLABLE_EMAIL_SCHEMA = {'anyOf': [EMAIL_SCHEMA, NULL_SCHEMA]}
GENDER_SCHEMA = {'enum': ['M', 'F']}
PAYMENT_SCHEMA = {'enum': ['DUMMY', 'TIGO CASH', 'MTN MOBILE MONEY',
                           'VODAFONE CASH', 'CREDIT CARD', 'MASTER CARD']}
COORDINATES_SCHEMA = {
    '$schema': DRAFT_7_SCHEMA,
    'type': 'object',
    'properties': {
        'longitude': FLOAT_SCHEMA,
        'latitude': FLOAT_SCHEMA
    },
    'required': ['longitude', 'latitude'],
    'additionalProperties': False
}

LOCATION_SCHEMA = {
    '$schema': DRAFT_7_SCHEMA,
    'type': 'object',
    'properties': {
        'longitude': FLOAT_SCHEMA,
        'latitude': FLOAT_SCHEMA,
        'name': STRING_SCHEMA
    },
    'required': ['longitude', 'latitude', 'name'],
    'additionalProperties': False
}

from .test_schema import TEST_VALIDATION_SCHEMA  # noqa
from .users_schema import USERS_REGISTRATION_SCHEMA, USER_UPDATE_SCHEMA  # noqa


SCHEMA = {
    'test_validation_SCHEMA': TEST_VALIDATION_SCHEMA,
    'USERS_REGISTRATION_SCHEMA': USERS_REGISTRATION_SCHEMA,
    'USER_UPDATE_SCHEMA': USER_UPDATE_SCHEMA,

}
