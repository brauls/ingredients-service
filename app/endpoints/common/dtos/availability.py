"""Availability of fruit and vegetables.
"""

from enum import IntEnum

class Availability(IntEnum):
    """Enum to define that availability of fruit and vegetables.
    """

    # fruit and vegetables that are beeing harvestet at a time
    FRESH = 1

    # fruit and vegetables that have been harvestet in the past and are now available from stock
    STOCK = 2

    # fruit and vegetables that are not currently available from local farmers
    IMPORTED = 3
