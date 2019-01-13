"""REST interface module for random point generation on 2D circles.
"""

from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest

from .common.services.ingredient_store import get_ingredients, get_ingredient, \
    create_ingredient, delete_ingredient
from .common.register_error_handler import register_error_handler

from .common.dtos.ingredient import IngredientSchema

API = Namespace(
    "ingredients",
    description="Manage ingredients",
    path="/ingredients"
)
register_error_handler(API)

# Define api models here, because reusing marshmallow schema is currently no supported.
# see issue: https://github.com/noirbizarre/flask-restplus/issues/438
INGREDIENT_POST_MODEL = API.model(
    "Ingredient",
    {"name" : fields.String("The name of the ingredient")}
)

@API.route("/")
class IngredientsApi(Resource):
    """REST interface class for managing ingredients.
    """

    # @API.param(name="center_x", description="The x coordinate of the circle center", _in="query")
    @API.doc("list_ingredients")
    def get(self):
        """Get a list of all available ingredients.

        Returns:
            list(IngredientDto): The list of ingredients.
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

        ingredients = get_ingredients()
        result = ingredient_schema.dump(ingredients)
        return jsonify(result.data)

    @API.doc("create_ingredient", responses={
        201: "Created",
        400: "Validation Error"
    })
    @API.expect(INGREDIENT_POST_MODEL)
    def post(self):
        """Create a new ingredient.

        Raises:
            BadRequest: Invalid ingredient definition supplied.

        Returns:
            IngredientDto: The created ingredient.
        """
        ingredient_schema = IngredientSchema()

        ingredient_json = request.json
        ingredient_validation = ingredient_schema.load(ingredient_json)
        if ingredient_validation.errors:
            raise BadRequest("Invalid ingredient definition supplied")
        ingredient_posted = ingredient_validation.data

        ingredient_created = create_ingredient(ingredient_posted)

        result = ingredient_schema.dump(ingredient_created)
        return result.data, 201
