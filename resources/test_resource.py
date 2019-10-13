from flask import make_response, jsonify, request
from flask_restful import Resource
from utils.validators import validate_json, validate_schema


class TestResource(Resource):

    def get(self):
        return {'message': 'response ok'}

    @staticmethod
    def test():
        return make_response(jsonify({'message': 'success'}), 201)

    @validate_json
    @validate_schema(schema_name='test_validation_SCHEMA')
    def post(self):
        data = request.get_json()
        return {'message': data}
