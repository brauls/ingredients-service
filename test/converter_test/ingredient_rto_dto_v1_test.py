"""Test the conversion between ingredient rtos and dtos.
"""

from app.endpoints.v1.payload.ingredient import Ingredient as IngredientRto
from app.endpoints.common.dtos.ingredient import Ingredient as IngredientDto

def test_ingredient_rto_to_dto_conversion():
    """Test the conversion from IngredientRto to IngredientDto.
    """
    ingredient_rto = IngredientRto("banana")
    ingredient_dto = ingredient_rto.to_ingredient_dto()
    assert ingredient_dto.name == "banana"

def test_ingredient_dto_to_rto_conversion():
    """Test the conversion from IngredientDto to IngredientRto.
    """
    ingredient_dto = IngredientDto("apple")
    ingredient_rto = IngredientRto.from_ingredient_dto(ingredient_dto)
    assert ingredient_rto.name == "apple"
