"""Test the conversion between ingredient rtos and dtos.
"""

import pytest

from app.endpoints.v1.payload.ingredient import Ingredient as IngredientRto
from app.endpoints.common.dtos.ingredient import Ingredient as IngredientDto
from app.endpoints.common.dtos.availability import Availability

# create test data
INGREDIENT_NAME = "pear"
AVAILABILITY_PER_MONTH_DTO = [
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
AVAILABILITY_PER_MONTH_RTO = [
    Availability.STOCK.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    Availability.FRESH.name,
    Availability.FRESH.name,
    Availability.FRESH.name,
    Availability.FRESH.name,
    Availability.STOCK.name,
    Availability.STOCK.name
]
AVAILABILITY_PER_MONTH_RTO_INVALID = [
    Availability.STOCK.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    Availability.IMPORTED.name,
    "UNKNOWN_NAME",
    Availability.FRESH.name,
    Availability.FRESH.name,
    Availability.FRESH.name,
    Availability.FRESH.name,
    Availability.STOCK.name,
    Availability.STOCK.name
]

def test_ingredient_rto_to_dto_conversion():
    """Test the conversion from IngredientRto to IngredientDto.
    """
    ingredient_rto = IngredientRto(INGREDIENT_NAME, AVAILABILITY_PER_MONTH_RTO)

    ingredient_dto = ingredient_rto.to_ingredient_dto()

    assert ingredient_dto.name == INGREDIENT_NAME
    assert ingredient_dto.availability_per_month == AVAILABILITY_PER_MONTH_DTO

def test_ingredient_dto_to_rto_conversion():
    """Test the conversion from IngredientDto to IngredientRto.
    """
    ingredient_dto = IngredientDto(INGREDIENT_NAME, AVAILABILITY_PER_MONTH_DTO)

    ingredient_rto = IngredientRto.from_ingredient_dto(ingredient_dto)

    assert ingredient_rto.name == INGREDIENT_NAME
    assert ingredient_rto.availability_per_month == AVAILABILITY_PER_MONTH_RTO

def test_conversion_with_invalid_enum_name():
    """Test the conversion from IngredientRto to IngredientDto using
    an invalid list of availability (unknown enum name)
    """
    ingredient_rto = IngredientRto(INGREDIENT_NAME, AVAILABILITY_PER_MONTH_RTO_INVALID)
    with pytest.raises(ValueError):
        ingredient_rto.to_ingredient_dto()
