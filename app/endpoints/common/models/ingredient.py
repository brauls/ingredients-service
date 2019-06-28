"""Ingredient database entity class.
"""

from . import DB

class Ingredient(DB.Model):
    """The Ingredient entity class.
    Defines ingredient as it is stored inside the database.
    """
    __tablename__ = "INGREDIENT"

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80), unique=True, nullable=False)
    availability = DB.relationship('IngredientAvailability', lazy='joined')

    def __repr__(self):
        return '<Ingredient %r>' % self.name

    def __str__(self):
        return """{} is the id, {} is the name.""".format(self.id, self.name)
