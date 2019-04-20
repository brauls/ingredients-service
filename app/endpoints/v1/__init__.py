"""Create the blueprint for version 1 of the ingredient API and assign the API to the blueprint.
"""

from flask import Blueprint

from .api import init_api

API_V1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

init_api(API_V1)
