"""REST interface module for posting new ingredients and requesting existing ones.
"""

from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest

from ..common.services.ingredient_store import get_ingredients, create_ingredient
from .register_error_handler import register_error_handler

from .payload.ingredient import Ingredient as IngredientRto, IngredientSchema

API = Namespace(
    "ingredients",
    description="Manage ingredients",
    path="/ingredients"
)
register_error_handler(API)

# Define api models here, because reusing marshmallow schema is currently not supported.
# see issue: https://github.com/noirbizarre/flask-restplus/issues/438
INGREDIENT_POST_MODEL = API.model(
    "Ingredient",
    {
        "name" : fields.String(
            description="The name of the ingredient", required=True, example="banana"),
        "availability_per_month" : fields.List(
            fields.Integer(
                min=1,
                max=3,
                description="The availability per month"),
            min_items=12,
            max_items=12,
            required=True,
            example=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    }
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
            list(IngredientRto): The list of ingredients.
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

        ingredient_dtos = get_ingredients()

        ingredient_rtos = [IngredientRto.from_ingredient_dto(ingredient_dto)
                           for ingredient_dto in ingredient_dtos]

        result = ingredient_schema.dump(ingredient_rtos)
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
            raise BadRequest("Invalid ingredient definition supplied.")
        ingredient_rto_posted = ingredient_validation.data

        ingredient_dto_posted = ingredient_rto_posted.to_ingredient_dto()

        ingredient_dto_created = create_ingredient(ingredient_dto_posted)

        ingredient_rto_created = IngredientRto.from_ingredient_dto(ingredient_dto_created)

        result = ingredient_schema.dump(ingredient_rto_created)
        return result.data, 201
