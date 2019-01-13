# pylint: disable=redefined-outer-name
"""Tests for the ingredients endpoint.
"""

import json
import pytest

from app import APP
from app.app import init_app
from app.endpoints.common.dtos.ingredient import IngredientSchema

@pytest.fixture(scope="module")
def test_client():
    """Create a test api client to use for the test cases-

    Returns:
        FlaskClient: The test client.
    """
    APP.config.from_object("app.config.TestConfig")
    init_app(APP)
    return APP.test_client()

def test_post_with_valid_input(test_client):
    """Test posting one new ingredient and requesting the list of ingredients.

    Args:
        test_client (FlaskClient): The test client.
    """

    # initially there should be no ingredients in the database
    init_ingredients_resp = test_client.get("/ingredients/")
    assert init_ingredients_resp.status_code == 200
    assert init_ingredients_resp.content_type == "application/json"
    init_ingredients = _parse_ingredients_response(init_ingredients_resp)
    assert not init_ingredients.data

    # next create a new ingredient
    post_ingredient_resp = test_client.post("/ingredients/", json={"name" : "apple"})
    assert post_ingredient_resp.status_code == 201
    assert post_ingredient_resp.content_type == "application/json"
    post_ingredient = _parse_ingredient_response(post_ingredient_resp)
    assert post_ingredient.data.name == "apple"

    # now there should be one ingredient in the database
    final_ingredients_resp = test_client.get("/ingredients/")
    assert init_ingredients_resp.status_code == 200
    assert init_ingredients_resp.content_type == "application/json"
    final_ingredients = _parse_ingredients_response(final_ingredients_resp)
    assert len(final_ingredients.data) == 1
    assert final_ingredients.data[0].name == "apple"

def test_post_with_invalid_input(test_client):
    """Test posting unexpected json data as a new ingredient.

    Args:
        test_client (FlaskClient): The test client.
    """
    post_ingredient_resp = test_client.post("/ingredients/", json={"foo" : "bar"})
    assert post_ingredient_resp.status_code == 400
    assert post_ingredient_resp.content_type == "application/json"
    post_ingredient = json.loads(post_ingredient_resp.get_data(as_text=True))
    assert post_ingredient["message"] == "Invalid ingredient definition supplied"

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
