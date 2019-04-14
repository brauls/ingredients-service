"""Entry point for the ingredients api during development.
"""
from flask_migrate import Migrate

from app import APP
from app.app import init_app

APP.config.from_object("app.config.DevelopmentConfig")
DB = init_app(APP)

MIGRATE = Migrate(APP, DB)

if __name__ == "__main__":
    APP.run()
