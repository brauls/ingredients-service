"""Fixture to yield a test client used in all tests that need one.
"""

import pytest

from app import APP
from app.app import init_app

@pytest.fixture(scope="session")
def test_client():
    """Create a test api client to use for the test cases.

    Returns:
        FlaskClient: The test client.
    """
    APP.config.from_object("app.config.TestConfig")
    database = init_app(APP)

    # create database schema for test module
    with APP.app_context():
        database.create_all()

    yield APP.test_client()
