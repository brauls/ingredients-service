"""Config module that contains configs for the different application environments
"""

import os

class Config(object):
    """The base application configuration
    """
    ENV = ""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """The production configuration
    """
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '')

class DevelopmentConfig(Config):
    """The development configuration
    """
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:137763@localhost:5432/ingredientsdb"

class TestConfig(Config):
    """The testing configuration
    """
    ENV = "test"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
