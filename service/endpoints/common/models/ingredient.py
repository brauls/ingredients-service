"""Ingredient database entity class.
"""

from . import DB

class Ingredient(DB.Model):
    __tablename__ = "ingredient"

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80), unique=True, nullable=False)

    def __repr__(self):
        return """{} is the name.""".format(self.name)
