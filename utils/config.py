__author__ = 'Ebenezer Adelwin Azumah'

import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'super-secret'
    JWT_SECRET_KEY = SECRET_KEY
    STORAGE_BUCKET = 'jedmedic-ce580.appspot.com/'
    FIREBASE_SERVICE_ACCOUNT = {
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
