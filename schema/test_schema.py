__author__ = 'Ebenezer Adelwin Azumah'

from . import DRAFT_7_SCHEMA, STRING_SCHEMA

TEST_VALIDATION_SCHEMA = {
    '$schema': DRAFT_7_SCHEMA,
    'type': 'object',
    'properties': {
        'item': STRING_SCHEMA
    },
    'additionalProperties': False,
    'required': ['item']
}
