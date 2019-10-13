from flask import request
from flask_restful import Resource
from utils.validators import validate_json, validate_schema


class UserResource(Resource):
    @validate_json
    @validate_schema('USERS_REGISTRATION_SCHEMA')
    def post(self):
        data = request.get_json()
        return {'data': data}, 201

    def get(self):
        data = request.get_json()
        return {'data': data}, 201

    @validate_json
    @validate_schema('USER_UPDATE_SCHEMA')
    def put(self):
        data = request.get_json()
        return {'data': data}
