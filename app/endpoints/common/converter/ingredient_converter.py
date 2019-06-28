"""Converts between ingredient entities and dtos.
"""

from ..dtos.ingredient import Ingredient as IngredientDto
from ..models.ingredient import Ingredient as IngredientEntity
from ..models.ingredient_availability import IngredientAvailability

def ingredient_entity_to_dto(ingredient_entity, ingredient_availability):
    """Convert an ingredient entity and ingredient availability to an ingredient dto.

    Args:
        ingredient_entity (IngredientEntity): An ingredient entity object.
        ingredient_availability (list(IngredientAvailability)):
          A list of ingredient availability per month.

    Returns:
        IngredientDto: The converted ingredient object.
    """
    availability_per_month = [ingredient_info.availability
                              for ingredient_info in ingredient_availability]
    return IngredientDto(ingredient_entity.name, availability_per_month)

def ingredient_dto_to_entity(ingredient_dto):
    """Convert an ingredient dto to an ingredient entity along with availability information.

    Args:
        ingredient_dto (IngredientDto): An ingredient dto object.

    Returns:
        tuple(IngredientEntity, list(IngredientAvailability)):
          The converted ingredient entity objects.
    """
    availability_per_month = [IngredientAvailability(month=idx, availability=val)
                              for idx, val in enumerate(ingredient_dto.availability_per_month)]
    return (IngredientEntity(name=ingredient_dto.name), availability_per_month)
