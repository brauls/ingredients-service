"""Ingredient dto.
"""

class Ingredient():
    """Class to represent an ingredient.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return """{} is the name.""".format(self.name)
