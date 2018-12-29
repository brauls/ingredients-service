"""CRUD operations for ingredients.
"""

import random

from ..dtos.ingredient import Ingredient as IngredientDto
from ..models.ingredient import Ingredient as IngredientEntity

from ..models import DB

def get_demo_ingredients():
    """Get a list of hard coded ingredients for demonstration.
    Returns:
      list(..models.ingredient.Ingredient): A list of hard coded ingredients.
    """
    return [
        IngredientDto("apple"),
        IngredientDto("banana"),
        IngredientDto("tomato")
    ]

def get_db_ingredients():
    ingredients = IngredientEntity.query.all()

    name = "demo" + str(len(ingredients))
    ingredient = IngredientEntity(name=name)

    DB.session.add(ingredient)
    DB.session.commit()

    return [IngredientDto(entity.name) for entity in ingredients]
