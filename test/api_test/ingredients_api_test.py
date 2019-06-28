"""Tests for the ingredients endpoint.
"""

import json

from app.endpoints.v1.payload.ingredient import IngredientSchema
from app.endpoints.common.dtos.availability import Availability

API_PATH = "/api/v1/ingredients/"
CONTENT_TYPE = "application/json"

# create test data
INGREDIENT_NAME = "pear"
AVAILABILITY_PER_MONTH = [
    Availability.STOCK.value,
    Availability.IMPORTED.value,
    Availability.IMPORTED.value,
    Availability.IMPORTED.value,
    Availability.IMPORTED.value,
    Availability.IMPORTED.value,
    Availability.FRESH.value,
    Availability.FRESH.value,
    Availability.FRESH.value,
    Availability.FRESH.value,
    Availability.STOCK.value,
    Availability.STOCK.value
]
AVAILABILITY_PER_MONTH_TOO_LESS = AVAILABILITY_PER_MONTH[0:11]
AVAILABILITY_PER_MONTH_TOO_MANY = [*AVAILABILITY_PER_MONTH, Availability.STOCK]
AVAILABILITY_PER_MONTH_INVALID_VALUE = [*AVAILABILITY_PER_MONTH_TOO_LESS, 99]

INGREDIENT_JSON_INVALID = {"foo" : "bar"}
INGREDIENT_JSON_MISSING_AVAILABILITY = {"name" : INGREDIENT_NAME}
INGREDIENT_JSON_TOO_LESS_MONTHS = {
    "name" : INGREDIENT_NAME, "availability_per_month" : AVAILABILITY_PER_MONTH_TOO_LESS}
INGREDIENT_JSON_TOO_MANY_MONTHS = {
    "name" : INGREDIENT_NAME, "availability_per_month" : AVAILABILITY_PER_MONTH_TOO_MANY}
INGREDIENT_JSON_INVALID_AVAILIBILITY_VALUE = {
    "name" : INGREDIENT_NAME, "availability_per_month" : AVAILABILITY_PER_MONTH_INVALID_VALUE}
INGREDIENT_JSON_VALID = {
    "name" : INGREDIENT_NAME, "availability_per_month" : AVAILABILITY_PER_MONTH}

def test_post_with_valid_input(test_client):
    """Test posting one new ingredient and requesting the list of ingredients.

    Args:
        test_client (FlaskClient): The test client.
    """

    # initially there should be no ingredients in the database
    init_ingredients_resp = test_client.get(API_PATH)
    assert init_ingredients_resp.status_code == 200
    assert init_ingredients_resp.content_type == CONTENT_TYPE
    init_ingredients = _parse_ingredients_response(init_ingredients_resp)
    assert not init_ingredients.data

    # next create a new ingredient
    post_ingredient_resp = test_client.post(API_PATH, json=INGREDIENT_JSON_VALID)
    assert post_ingredient_resp.status_code == 201
    assert post_ingredient_resp.content_type == CONTENT_TYPE
    post_ingredient = _parse_ingredient_response(post_ingredient_resp)
    assert post_ingredient.data.name == INGREDIENT_NAME
    assert post_ingredient.data.availability_per_month == AVAILABILITY_PER_MONTH

    # now there should be one ingredient in the database
    final_ingredients_resp = test_client.get(API_PATH)
    assert final_ingredients_resp.status_code == 200
    assert final_ingredients_resp.content_type == CONTENT_TYPE
    final_ingredients = _parse_ingredients_response(final_ingredients_resp)
    assert len(final_ingredients.data) == 1
    assert final_ingredients.data[0].name == INGREDIENT_NAME
    assert final_ingredients.data[0].availability_per_month == AVAILABILITY_PER_MONTH

def test_post_with_invalid_input(test_client):
    """Test posting unexpected json data as a new ingredient.

    Args:
        test_client (FlaskClient): The test client.
    """
    post_ingredient_resp = test_client.post(API_PATH, json=INGREDIENT_JSON_INVALID)
    assert post_ingredient_resp.status_code == 400
    assert post_ingredient_resp.content_type == CONTENT_TYPE
    post_ingredient = json.loads(post_ingredient_resp.get_data(as_text=True))
    assert post_ingredient["message"] == "Invalid ingredient definition supplied."

def test_post_with_too_less_months(test_client):
    """Test posting an ingredient along with availability information for less than 12 months.

    Args:
        test_client (FlaskClient): The test client.
    """
    post_ingredient_resp = test_client.post(API_PATH, json=INGREDIENT_JSON_TOO_LESS_MONTHS)
    assert post_ingredient_resp.status_code == 400
    assert post_ingredient_resp.content_type == CONTENT_TYPE
    post_ingredient = json.loads(post_ingredient_resp.get_data(as_text=True))
    assert post_ingredient["message"] == "Invalid ingredient definition supplied."

def test_post_with_too_many_months(test_client):
    """Test posting an ingredient along with availability information for more than 12 months.

    Args:
        test_client (FlaskClient): The test client.
    """
    post_ingredient_resp = test_client.post(API_PATH, json=INGREDIENT_JSON_TOO_MANY_MONTHS)
    assert post_ingredient_resp.status_code == 400
    assert post_ingredient_resp.content_type == CONTENT_TYPE
    post_ingredient = json.loads(post_ingredient_resp.get_data(as_text=True))
    assert post_ingredient["message"] == "Invalid ingredient definition supplied."

def test_post_with_invalid_availability_value(test_client):
    """Test posting an ingredient along with invalid availability information.

    Args:
        test_client (FlaskClient): The test client.
    """
    post_ingredient_resp = test_client.post(
        API_PATH, json=INGREDIENT_JSON_INVALID_AVAILIBILITY_VALUE)
    assert post_ingredient_resp.status_code == 400
    assert post_ingredient_resp.content_type == CONTENT_TYPE
    post_ingredient = json.loads(post_ingredient_resp.get_data(as_text=True))
    assert post_ingredient["message"] == "Invalid ingredient definition supplied."

def _parse_ingredients_response(response):
    """Parses an ingredients response of a test client.

    Args:
        response (flask.wrappers.Response): A test response possibly containing ingredients.

    Returns:
        list(IngredientDto): A list of ingredients extracted from the response.
    """
    ingredients_from_json = json.loads(response.get_data(as_text=True))
    ingredients_schema = IngredientSchema(many=True)
    ingredients = ingredients_schema.load(ingredients_from_json)
    return ingredients

def _parse_ingredient_response(response):
    """Parses an ingredient response of a test client.

    Args:
        response (flask.wrappers.Response): A test response possibly containing one ingredient.

    Returns:
        IngredientDto: An ingredient extracted from the response.
    """
    ingredients_from_json = json.loads(response.get_data(as_text=True))
    ingredient_schema = IngredientSchema()
    ingredient = ingredient_schema.load(ingredients_from_json)
    return ingredient
