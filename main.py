"""Entry point for the ingredients api.
"""

from service import APP

if __name__ == "__main__":
    APP.config.from_object("service.config.DevelopmentConfig")
    APP.run()
