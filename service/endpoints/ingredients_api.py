"""REST interface module for random point generation on 2D circles.
"""

from flask import request, jsonify
from flask_restplus import Namespace, Resource
# from werkzeug.exceptions import BadRequest

from .common.services.ingredient_store import get_demo_ingredients
from .common.register_error_handler import register_error_handler

from .common.models.ingredient import IngredientSchema

API = Namespace(
    "ingredients",
    description="Manage ingredients",
    path="/ingredients"
)
register_error_handler(API)

@API.route("/")
class Ingredients_API(Resource):
    """REST interface class for managing ingredients.
    """

    # @API.param(name="center_x", description="The x coordinate of the circle center", _in="query")
    # @API.param(name="center_y", description="The y coordinate of the circle center", _in="query")
    # @API.param(name="radius", description="The radius of the circle", _in="query")
    # @API.param(name="num_points", description="The rnumber of random points to create", _in="query")
    @API.doc("list_ingredients")
    def get(self):
        """Get a list of available ingredients.
        """

        ingredient_schema = IngredientSchema(many=True)

        # cannot access payload through namespace at the moment, so use the flask request
        # flask_restplus issue: https://github.com/noirbizarre/flask-restplus/issues/370
        # circle_validation = circle_schema.load(request.args)
        # point_count_validation = point_count_schema.load(request.args)
        # if circle_validation.errors:
        #     raise BadRequest("Invalid circle definition supplied")
        # if point_count_validation.errors:
        #     raise BadRequest("Invalid point count definition supplied")

        # circle = circle_validation.data
        # point_count = point_count_validation.data

        ingredients = get_demo_ingredients()
        result = ingredient_schema.dump(ingredients)
        return jsonify(result.data)
