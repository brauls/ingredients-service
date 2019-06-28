"""Test the conversion between ingredient dtos and entities.
"""

from app.endpoints.common.models.ingredient import Ingredient as IngredientEntity
from app.endpoints.common.models.ingredient_availability import IngredientAvailability
from app.endpoints.common.dtos.ingredient import Ingredient as IngredientDto
from app.endpoints.common.dtos.availability import Availability
from app.endpoints.common.converter.ingredient_converter \
    import ingredient_dto_to_entity, ingredient_entity_to_dto

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
INGREDIENT_AVAILABILITY_ENTITIES = [
    IngredientAvailability(id=idx, ingredient_id=1, month=idx-1, availability=availability)
    for idx, availability in enumerate(AVAILABILITY_PER_MONTH)]

def test_ingredient_entity_to_dto_conversion():
    """Test the conversion from IngredientEntity and IngredientAvailability to IngredientDto.
    """
    ingredient_entity = IngredientEntity(id=1, name=INGREDIENT_NAME)

    ingredient_dto = ingredient_entity_to_dto(ingredient_entity, INGREDIENT_AVAILABILITY_ENTITIES)

    assert ingredient_dto.name == INGREDIENT_NAME
    assert ingredient_dto.availability_per_month == AVAILABILITY_PER_MONTH

def test_ingredient_dto_to_entity_conversion():
    """Test the conversion from IngredientDto to IngredientEntity and IngredientAvailability.
    """
    ingredient_dto = IngredientDto(INGREDIENT_NAME, AVAILABILITY_PER_MONTH)

    converted_ingredient_tuple = ingredient_dto_to_entity(ingredient_dto)
    ingredient_entity = converted_ingredient_tuple[0]
    ingredient_availability_entities = converted_ingredient_tuple[1]

    assert ingredient_entity.name == INGREDIENT_NAME
    expected_ingredient_availability = [
        IngredientAvailability(id=1, ingredient_id=1, month=0, availability=Availability.STOCK),
        IngredientAvailability(id=2, ingredient_id=1, month=1, availability=Availability.IMPORTED),
        IngredientAvailability(id=3, ingredient_id=1, month=2, availability=Availability.IMPORTED),
        IngredientAvailability(id=4, ingredient_id=1, month=3, availability=Availability.IMPORTED),
        IngredientAvailability(id=5, ingredient_id=1, month=4, availability=Availability.IMPORTED),
        IngredientAvailability(id=6, ingredient_id=1, month=5, availability=Availability.IMPORTED),
        IngredientAvailability(id=7, ingredient_id=1, month=6, availability=Availability.FRESH),
        IngredientAvailability(id=8, ingredient_id=1, month=7, availability=Availability.FRESH),
        IngredientAvailability(id=9, ingredient_id=1, month=8, availability=Availability.FRESH),
        IngredientAvailability(id=10, ingredient_id=1, month=9, availability=Availability.FRESH),
        IngredientAvailability(id=11, ingredient_id=1, month=10, availability=Availability.STOCK),
        IngredientAvailability(id=12, ingredient_id=1, month=11, availability=Availability.STOCK)
    ]
    for idx, val in enumerate(expected_ingredient_availability):
        assert val.month == ingredient_availability_entities[idx].month
        assert val.availability == ingredient_availability_entities[idx].availability
