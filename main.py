"""Entry point for the ingredients api.
"""

from app import APP
from app.app import init_app

if __name__ == "__main__":
    APP.config.from_object("app.config.DevelopmentConfig")
    init_app(APP)
    APP.run()
