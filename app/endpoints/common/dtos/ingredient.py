"""Ingredient dto.
"""

class Ingredient():
    """Class to represent an ingredient.
    """
    def __init__(self, name, availability_per_month):
        self.name = name
        self.availability_per_month = availability_per_month

    def __repr__(self):
        return """{} is the name.""".format(self.name)
