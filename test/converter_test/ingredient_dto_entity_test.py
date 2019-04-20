"""Test the conversion between ingredient dtos and entities.
"""

from app.endpoints.common.models.ingredient import Ingredient as IngredientEntity
from app.endpoints.common.dtos.ingredient import Ingredient as IngredientDto
from app.endpoints.common.converter.ingredient_converter \
    import ingredient_dto_to_entity, ingredient_entity_to_dto

def test_ingredient_entity_to_dto_conversion():
    """Test the conversion from IngredientEntity to IngredientDto.
    """
    ingredient_entity = IngredientEntity(id=1, name="banana")
    ingredient_dto = ingredient_entity_to_dto(ingredient_entity)
    assert ingredient_dto.name == "banana"

def test_ingredient_dto_to_entity_conversion():
    """Test the conversion from IngredientDto to IngredientEntity.
    """
    ingredient_dto = IngredientDto("apple")
    ingredient_entity = ingredient_dto_to_entity(ingredient_dto)
    assert ingredient_entity.name == "apple"
