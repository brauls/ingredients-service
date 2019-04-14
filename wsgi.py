"""Entry point for the ingredients api for wsgi server.
"""
from flask_migrate import Migrate

from app import APP
from app.app import init_app

APP.config.from_object("app.config.ProductionConfig")
DB = init_app(APP)

MIGRATE = Migrate(APP, DB)
