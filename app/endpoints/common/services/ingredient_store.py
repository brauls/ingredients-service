"""CRUD operations for ingredients.
"""

from ..models.ingredient import Ingredient as IngredientEntity
from ..models.ingredient_availability import IngredientAvailability
from ..converter.ingredient_converter import ingredient_entity_to_dto, ingredient_dto_to_entity

from ..models import DB

def get_ingredients():
    """Find all available ingredients.

    Returns:
        list(IngredientDto): A list of all ingredients.
    """
    ingredient_entities = IngredientEntity.query.all()
    return [ingredient_entity_to_dto(entity, entity.availability) for entity in ingredient_entities]

def get_ingredient(name):
    """Find an ingredient by its name.

    Args:
        name (string): The name of the ingredient.

    Returns:
        IngredientDto: The ingredient with the given name, or None.
    """
    ingredient_entity = IngredientEntity.query.filter_by(name=name).first()
    if ingredient_entity is None:
        return None
    ingredient_availability = ingredient_entity.ingredient_availability

    return ingredient_entity_to_dto(ingredient_entity, ingredient_availability)

def create_ingredient(ingredient_dto):
    """Create a new ingredient inside the database.

    Args:
        ingredient_dto (IngredientDto): The ingredient to be created.
    """
    (ingredient_entity, ingredient_availability) = ingredient_dto_to_entity(ingredient_dto)
    ingredient_entity.availability = ingredient_availability

    DB.session.add(ingredient_entity)
    DB.session.commit()

    return ingredient_entity_to_dto(ingredient_entity, ingredient_availability)

def delete_ingredient(name):
    """Delete an existing ingredient from the database.

    Args:
        name (string): The name of the ingredient to be deleted.
    """
    ingredient_entity = IngredientEntity.query.filter_by(name=name).first()
    if ingredient_entity is not None:
        DB.session.delete(ingredient_entity)
        DB.session.commit()
  