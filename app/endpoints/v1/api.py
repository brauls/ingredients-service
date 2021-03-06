"""API initialization module for Ingredients v1.
"""

from flask_restplus import Api

from .ingredients_api import API as ingredients_api

def init_api(blueprint):
    """Create the api along with the available namespaces.

    Returns:
        Api: The initialized api object
    """
    api = Api(
        blueprint,
        title="Ingredients API",
        version="1.0.0",
        description="Manage ingredients and their availability"
    )
    api.add_namespace(ingredients_api)
