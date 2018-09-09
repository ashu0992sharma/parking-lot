from src.abs_parking import AbsParking

import sys


class Exit(AbsParking):
    """Parking Lot class to create a Parking lot"""
    name = 'exit'

    def __init__(self, args):
        """
        constructor to initialize exit object
        :param args:
        """
        pass

    def execute(self, parking_lot=None):
        sys.exit()