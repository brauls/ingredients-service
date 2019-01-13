"""Config module that contains configs for the different application environments
"""

class Config(object):
    """The base application configuration
    """
    ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """The production configuration
    """
    pass

class DevelopmentConfig(Config):
    """The development configuration
    """
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:137763@localhost:5432/ingredientsdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    """The testing configuration
    """
    ENV = "test"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
