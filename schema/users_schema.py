__author__ = 'Ebenezer Adelwin Azumah'

from . import DRAFT_7_SCHEMA, STRING_SCHEMA, EMAIL_SCHEMA, LOCATION_SCHEMA

USERS_REGISTRATION_SCHEMA = {
    '$schema': DRAFT_7_SCHEMA,
    'type': 'object',
    'properties': {
        'first_name': STRING_SCHEMA,
        'surname': STRING_SCHEMA,
        'other_names': STRING_SCHEMA,
        'email': EMAIL_SCHEMA,
        'phone': STRING_SCHEMA,
        'nationality': STRING_SCHEMA,
        'religion': STRING_SCHEMA,
        'marital_status': STRING_SCHEMA,
        'occupation': STRING_SCHEMA,
        'password': STRING_SCHEMA,
        'location': LOCATION_SCHEMA,
        'gender': STRING_SCHEMA,
        'date_of_birth': STRING_SCHEMA,
    },
    'additionalProperties': False,
    'required': ['first_name', 'surname', 'email', 'password']
}
USERS_VERIFICATION_SCHEMA = {
    '$schema': DRAFT_7_SCHEMA,
    'type': 'object',
    'properties': {
        'email': EMAIL_SCHEMA,
        'password': STRING_SCHEMA,
        'device_id': STRING_SCHEMA
    },
    'additionalProperties': False,
    'required': ['phone']
}

USER_UPDATE_SCHEMA = {
    '$schema': DRAFT_7_SCHEMA,
    'type': 'object',
    'properties': {
        'id': STRING_SCHEMA,
        'first_name': STRING_SCHEMA,
        'surname': STRING_SCHEMA,
        'other_names': STRING_SCHEMA,
        'email': EMAIL_SCHEMA,
        'phone': STRING_SCHEMA,
        'marital_status': STRING_SCHEMA,
        'occupation': STRING_SCHEMA,
    },
    'additionalProperties': False,
    'required': ['id']
}


# Surname
# other names
# Gender
# Date of Birth
# Current Location
# Phone number
# Emails
# nationality
# Religion
# Marital Status
# Occupation
# Address Digital address (GP code)
# Emergency contact
