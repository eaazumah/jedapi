__author__ = 'Ebenezer Adelwin, Azumah'

from typing import Dict


class BaseError(Exception):
    """Base Exception class to serialise error objects to json response

    Arguments:
        message -- [error message]
        error_code -- [status code response]
        payload -- [additional data to help know what went wrong]


    Returns:
        Serialised response json object
    """

    def __init__(self, message: str, error_code: int = 400, payload: [Dict, None] = None, *args) -> None:
        super(BaseError, self).__init__(*args)
        self.message = message
        self.payload = payload
        self.error_code = error_code

    def to_dict(self) -> Dict:
        response = {'message': self.message}  # type: dict
        if self.payload:
            response['data'] = self.payload
        return response


class JSONDataValidationError(BaseError):
    """
    Error handler for invalid json structure as expected by the server
    """

    def __init__(self, message: str, payload: [Dict, None], error_code: int = 442) -> None:
        # type (str, str, int) -> None
        super(JSONDataValidationError, self).__init__(
            message=message, payload=payload, error_code=error_code)


class AuthenticationError(BaseError):
    """
    Error handler for authentication
    """

    def __init__(self):
        super(AuthenticationError, self).__init__(
            message='Authentication Failed', error_code=401)


class PrivilegesError(BaseError):
    """Error handler for permissions"""

    def __init__(self):
        super(PrivilegesError, self).__init__(
            message='Privileges Error, Access Denied', error_code=401)


class InvalidAuthorizationHeader(BaseError):
    """Error handler for invalid authorization header"""

    def __init__(self):
        super(InvalidAuthorizationHeader, self).__init__(
            message='Invalid Authorization Header', error_code=401)
