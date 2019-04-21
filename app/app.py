"""Entry module that inits the flask app.
"""

from flask import Flask

from .endpoints.common.models import DB
from .register_templates import register_api_overview
from .endpoints.v1 import API_V1

def create_app():
    """Create the flask app.

    Returns:
        Flask: The initialized flask app
    """
    flask_app = Flask(__name__)
    return flask_app

def init_app(flask_app):
    """Initially configure the flask app.

    Initialize the SQLAlchemy object.
    Initialize the ingredients api versions.
    Initialize the start page containing the overview of all API versions.

    Before calling this function the application configuration must be loaded
    into the application object through flask_app.config.from_object().

    Args:
        flask_app (Flask): The flask application object.

    Returns:
        SQLAlchemy: The SQLAlchemy database object.
    """
    with flask_app.app_context():
        DB.init_app(flask_app)

    flask_app.register_blueprint(API_V1)

    register_api_overview(flask_app)

    return DB
