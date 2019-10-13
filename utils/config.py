__author__ = 'Ebenezer Adelwin Azumah'

import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'super-secret'
    JWT_SECRET_KEY = SECRET_KEY
    STORAGE_BUCKET = 'jedmedic-ce580.appspot.com/'
    FIREBASE_SERVICE_ACCOUNT = {
        "type": "service_account",
        "project_id": "jedmedic-ce580",
        "private_key_id": "7c14f604a6909fd15d72fcc76c3be13c09c25e8f",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCudTQZxoO1Lrtj\nDful6kCrE7ioyRTgvjEZG/yi9/i7h+6++lpOXjVt0EEsY0Z0CpaaqUEmfSBQo4g8\nn38FdHNvPflqkqjRd55K9M18ohScJrRkCvz8FWyBFFWhEBQJivEd3Pg9XGodzgQA\nDuCFo0NENlpi8zG48XV1DxcnJ/qgvRzFPjUpLyW7963RJO8hdKh5rUMiQL6sCd/H\nEQL7HUhGNYZk+zspWwWkOKfverE9JSuqXX0OowO+Dmev0D5j50eCEygFA7eoVyo1\njoG62GQC2wS++zoAvxllQXOefFLGlFCX69UL3Zkk4nrmg2sm6ICSevI2pXfRWAio\nxW0a/DdvAgMBAAECggEAAiyHt60s8FG4GBCRNYy+aDiuBmcVvC834WjjNGIEAXeS\nLA277loSLwoh+xxJlndDT9i9bRiwvGXX9BlwtcVbuDkney0qBAzfi249g/NpGlZe\nd8NYn7OMpJciR12HQmSELgEWPtLV/QUXhlX+dOvckg8IqqRT1vV7UeLG67/9yYmh\nzAgFDGkEhpTIvZg9nKRT25wCPPScK4pyjYh756orObuw9Gmv+GfX32tO0VM1G1cu\nXpAYEQTUSiT5iXbNEc+hUA/OWublxd9feBCcCIa811u0KdTAowQqibpras+TD5+D\nt5H414kI2UZCQDGNn0GAbRG3ubW5+++DVx8DwTZCgQKBgQDmi/o+woY/pgdsJrNq\nOqYJWu3urZdLQwn9lDGXyAdMf9B7On7n28vvpN6YvFwwFdkoFKLGcNcjVojkOqWH\nohh3oLU4j2HdcYecEUCsE9OLGk6PWCfsPckxZJPLDgLvfa3IziWzZhMHm9O2mA/+\nkM6kBdxZZKPQSUAlSPPIU9+2IQKBgQDBt/btsrUk58LpW4875mh7nQNLy1ThE8BT\nDcRtc6MvAXUg3gG+RXeXy8geDD23UQCpzcyygYMo0vVq3ph4Sg1c1ES6KCBIUF1z\nJpQFXJbpzkFgO0ePCSKPAq1MpUUu35p1r1S8POwYBXioyc9u1yjMfOanoNvsz03S\nqoW37tAbjwKBgBX/MxA75S07fSfPhXzUPbVUzLDiNTZEHjbopdayiie9ZjnrueIL\ncaja1TZDepRH8WFGnsVKTOydPBBynAqV57m6RrAv1gmX5HV6m+4PMjbqeqZopd5/\ngqvIyeUs4BDTr/oh2S0FxzkJoCii15vVWzIBMSYCWTLtWkZ0cHYjsouhAoGBAJqZ\nxfDX0ad9a1mvn7VPYg1dNrcztC7ZA4GFGEG9qvslr6Omaj++0v4LPU91t39onx3l\nR7sij1lyWziKI6bEerueEKd8xJ7RvHLc0/8fcLVxzU0OokJuKO13VnU35OnOvEe1\nwOtlt4pIO46BWRH9lurzt2UKhNoOa+539rXfWqjTAoGBAMN0waVygq19/lg6d/md\nCn/6dJwyhfcsA55MVLQar4uTkxECUAeiz66HRSujX9eqV/kI//1awgs4AAXEovIO\nT6bhwmVtEXGkO7A1X151LS+/33WxLtAxm9UO9IyN03TY0vPRK+GK6vrpx7MJU+ha\nnY2xGPncPlT7Picbb2kyhad5\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-1km9q@jedmedic-ce580.iam.gserviceaccount.com",
        "client_id": "117954948698970495670",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1km9q%40jedmedic-ce580.iam.gserviceaccount.com"
    }

    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = 'erranda2019@gmail.com'
    # MAIL_PASSWORD = 'silqpexkrffowcqb'

    # ONE_SIGNAL_APP_ID = '74f2c3ca-7b2e-4f83-8477-d952954d6a38'
    # ONE_SIGNAL_USER_AUTH_KEY = 'ZGZiZDI3MzMtYTZkYy00ZGRkLWE3MTUtYTkxZWZhYTFlMmY1'
    # ONE_SIGNAL_APP_AUTH_KEY = 'MzhlZGExY2QtYzI2Mi00ZTliLTkxMGMtMzk2MzNhYjNkMjUw'


class Development(Config):
    DEBUG = True
    ENV = 'development'


class Production(Config):
    ENV = 'production'
    SECRET_KEY = os.environ.get('SECRET-KEY')
