"""Entry point for the ingredients api.
"""

from service import APP
from service.app import init_db

if __name__ == "__main__":
    APP.config.from_object("service.config.DevelopmentConfig")
    init_db(APP)
    APP.run()
