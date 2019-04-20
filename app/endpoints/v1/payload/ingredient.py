"""Ingredient rto and schema.
"""

from marshmallow import Schema, fields, post_load

from ...common.dtos.ingredient import Ingredient as IngredientDto

class Ingredient():
    """Class to represent an ingredient.
    """
    def __init__(self, name):
        self.name = name

    def to_ingredient_dto(self):
        """Convert this Ingredient instance into an IngredientDto.

        Returns:
            IngredientDto: This ingredient transformed into IngredientDto.
        """
        return IngredientDto(self.name)

    @staticmethod
    def from_ingredient_dto(ingredient_dto):
        """Create an Ingredient instance from an IngredientDto instance.

        Returns:
            Ingredient: This ingredient_dto transformed into Ingredient.
        """
        return Ingredient(ingredient_dto.name)

    def __repr__(self):
        return """{} is the name.""".format(self.name)

class IngredientSchema(Schema):
    """Schema class for Ingredient class used for validation.
    """
    name = fields.String(required=True, description="The name of the ingredient")

    @post_load
    def _create_ingredient(self, data):
        """Create an Ingredient instance after data was loaded successfully
        through IngredientSchema.
        """
        return Ingredient(**data)
