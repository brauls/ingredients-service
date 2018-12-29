"""Entry module that inits the flask app.
"""

from flask import Flask

from .endpoints.api import init_api
from .endpoints.common.models import DB

def create_app():
    """Create the flask app and initialize the ingredients api.

    Returns:
        Flask: The initialized flask app
    """
    flask_app = Flask(__name__)
    api = init_api()
    api.init_app(flask_app)
    return flask_app

def init_db(flask_app):
    """Configure the Flask application to support the SQLAlchemy object.
    """
    with flask_app.app_context():
        DB.init_app(flask_app)
        DB.create_all()
