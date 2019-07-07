"""Ingredient rto and schema.
"""

from marshmallow import Schema, fields, post_load

from ...common.dtos.ingredient import Ingredient as IngredientDto
from ...common.dtos.availability import Availability

class Ingredient():
    """Class to represent an ingredient.
    """
    def __init__(self, name, availability_per_month):
        self.name = name
        self.availability_per_month = availability_per_month

    def to_ingredient_dto(self):
        """Convert this Ingredient instance into an IngredientDto.

        Returns:
            IngredientDto: This ingredient transformed into IngredientDto.
        """
        availability = [_convert_availability_string_to_enum_value(a)
                        for a in self.availability_per_month]
        return IngredientDto(self.name, availability)

    @staticmethod
    def from_ingredient_dto(ingredient_dto):
        """Create an Ingredient instance from an IngredientDto instance.

        Returns:
            Ingredient: This ingredient_dto transformed into Ingredient.
        """
        availability = [_convert_availability_enum_value_to_string(a)
                        for a in ingredient_dto.availability_per_month]
        return Ingredient(ingredient_dto.name, availability)

    def __repr__(self):
        return """{} is the name. {} is the availability per month.""".format(
            self.name, self.availability_per_month)

class IngredientSchema(Schema):
    """Schema class for Ingredient class used for validation.
    """
    name = fields.String(required=True, description="The name of the ingredient")
    availability_per_month = fields.List(
        fields.String(
            validate=lambda val: val in _list_of_availability_strings(),
            description="The availability per month"),
        validate=lambda val: len(val) == 12,
        required=True)

    @post_load
    def _create_ingredient(self, data):
        """Create an Ingredient instance after data was loaded successfully
        through IngredientSchema.
        """
        return Ingredient(**data)

def _list_of_availability_strings():
    """Returns a list of all possible availability values as string.
    """
    names = [availability.name for availability in Availability]
    return names

def _convert_availability_enum_value_to_string(availability):
    """Convert an availability value to its string representation.

    Args:
        availability ([int]): One availability value.
    """
    return Availability(availability).name

def _convert_availability_string_to_enum_value(availability_string):
    """Convert an availability string to an availability enum entry.

    Args:
        availability_string ([string]): The string representation of an enum entry.
    """
    availability_mappings = [(availability.name, availability.value)
                             for availability in Availability]
    availability_dict = dict(availability_mappings)

    if not availability_string in availability_dict:
        raise ValueError("Invalid availability '" + availability_string + "'")
    return availability_dict[availability_string]
