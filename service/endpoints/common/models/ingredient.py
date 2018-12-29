"""Ingredient model and schema.
"""

from marshmallow import Schema, fields, post_load

class Ingredient(object):
    """Class to represent an ingredient.
    """
    def __init__(self, name):
        self.name = name

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
