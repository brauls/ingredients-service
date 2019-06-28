"""Ingredient's availability database entity class.
"""

from . import DB

class IngredientAvailability(DB.Model):
    """The IngredientAvailability entity class.
    Defines the availability for one ingredient in one month.
    """
    __tablename__ = "INGREDIENT_AVAILABILITY"

    id = DB.Column(DB.Integer, primary_key=True)
    ingredient_id = DB.Column(DB.Integer, DB.ForeignKey('INGREDIENT.id'),
                              unique=False, nullable=False)
    # 0 = january, 11 = december
    month = DB.Column(DB.Integer, unique=False, nullable=False)
    availability = DB.Column(DB.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<IngredientAvailability %r %r %r>' % (self.ingredient_id, self.month, self.availability)

    def __str__(self):
        return """{} is the id, {} is the ingredient. {} is the month. {} is the availability.""".format(
            self.id, self.name, self.month, self.availability)
