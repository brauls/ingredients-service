"""Test the conversion between ingredient rtos and dtos.
"""

from app.endpoints.v1.payload.ingredient import Ingredient as IngredientRto
from app.endpoints.common.dtos.ingredient import Ingredient as IngredientDto
from app.endpoints.common.dtos.availability import Availability

# create test data
INGREDIENT_NAME = "pear"
AVAILABILITY_PER_MONTH = [
    Availability.STOCK,
    Availability.IMPORTED,
    Availability.IMPORTED,
    Availability.IMPORTED,
    Availability.IMPORTED,
    Availability.IMPORTED,
    Availability.FRESH,
    Availability.FRESH,
    Availability.FRESH,
    Availability.FRESH,
    Availability.STOCK,
    Availability.STOCK
]

def test_ingredient_rto_to_dto_conversion():
    """Test the conversion from IngredientRto to IngredientDto.
    """
    ingredient_rto = IngredientRto(INGREDIENT_NAME, AVAILABILITY_PER_MONTH)

    ingredient_dto = ingredient_rto.to_ingredient_dto()

    assert ingredient_dto.name == INGREDIENT_NAME
    assert ingredient_dto.availability_per_month == AVAILABILITY_PER_MONTH

def test_ingredient_dto_to_rto_conversion():
    """Test the conversion from IngredientDto to IngredientRto.
    """
    ingredient_dto = IngredientDto(INGREDIENT_NAME, AVAILABILITY_PER_MONTH)

    ingredient_rto = IngredientRto.from_ingredient_dto(ingredient_dto)

    assert ingredient_rto.name == INGREDIENT_NAME
    assert ingredient_rto.availability_per_month == AVAILABILITY_PER_MONTH
