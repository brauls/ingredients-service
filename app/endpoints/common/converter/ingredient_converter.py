"""Converts between ingredient entities and dtos.
"""

from ..dtos.ingredient import Ingredient as IngredientDto
from ..models.ingredient import Ingredient as IngredientEntity

def ingredient_entity_to_dto(ingredient_entity):
    """Convert an ingredient entity to an ingredient dto.

    Args:
      ingredient_entity (IngredientEntity): An ingredient entity object.
    """
    return IngredientDto(ingredient_entity.name)

def ingredient_dto_to_entity(ingredient_dto):
    """Convert an ingredient dto to an ingredient entity.

    Args:
      ingredient_dto (IngredientDto): An ingredient dto object.
    """
    return IngredientEntity(name=ingredient_dto.name)
