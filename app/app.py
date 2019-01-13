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
    return flask_app

def init_app(flask_app):
    """Initially configure the flask app.

    Initialize the ingredients api and the SQLAlchemy obkect.

    Args:
        flask_app (Flask): The flask application object.
    """
    with flask_app.app_context():
        DB.init_app(flask_app)
        DB.create_all()
        
        api = init_api()
        api.init_app(flask_app)
