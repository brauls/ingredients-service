"""CRUD operations for ingredients.
"""

from ..models.ingredient import Ingredient

def get_demo_ingredients():
    """Get a list of hard coded ingredients for demonstration.
    Returns:
      list(..models.ingredient.Ingredient): A list of hard coded ingredients.
    """
    return [
        Ingredient("apple"),
        Ingredient("banana"),
        Ingredient("tomato")
    ]
