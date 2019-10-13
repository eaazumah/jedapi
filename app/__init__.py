__author__ = 'Ebenezer Adelwin Azumah'

import firebase_admin
from firebase_admin import credentials
from flask import Flask
from utils import load_config
from flask_cors import CORS

def create_app():
    """Create flask app

    Returns:
        Flask -- Flask app
    """

    app: Flask = Flask(__name__)
    app.config.from_object(load_config())
    # mail = Mail(app)
    CORS(app)
    return app

def init_firebase():
    # .- get path to serviceAccount.json
    service_account_path = load_config().FIREBASE_SERVICE_ACCOUNT

    cred = credentials.Certificate(service_account_path)

    try:
        firebase_admin.get_app()
    except ValueError:
        return firebase_admin.initialize_app(credential=cred, options={'storageBucket': load_config().STORAGE_BUCKET})

