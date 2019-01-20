"""Entry point for the ingredients api for wsgi server.
"""

from app import APP
from app.app import init_app

APP.config.from_object("app.config.ProductionConfig")
init_app(APP)
