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
        return IngredientDto(self.name, self.availability_per_month)

    @staticmethod
    def from_ingredient_dto(ingredient_dto):
        """Create an Ingredient instance from an IngredientDto instance.

        Returns:
            Ingredient: This ingredient_dto transformed into Ingredient.
        """
        return Ingredient(ingredient_dto.name, ingredient_dto.availability_per_month)

    def __repr__(self):
        return """{} is the name. {} is the availability per month.""".format(
            self.name, self.availability_per_month)

class IngredientSchema(Schema):
    """Schema class for Ingredient class used for validation.
    """
    name = fields.String(required=True, description="The name of the ingredient")
    availability_per_month = fields.List(
        fields.Integer(
            validate=lambda val: val in list(map(int, Availability)),
            description="The availability per month"),
        validate=lambda val: len(val) == 12,
        required=True)

    @post_load
    def _create_ingredient(self, data):
        """Create an Ingredient instance after data was loaded successfully
        through IngredientSchema.
        """
        return Ingredient(**data)
