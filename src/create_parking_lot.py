from src.abs_parking import AbsParking


class CreateParkingLot(AbsParking):
    """Parking Lot class to create a Parking lot"""
    name = 'create_parking_lot'

    def __init__(self, args):
        """
        construction to initialize parking lot object
        :param args: quantity of the slots in parking lot
        """
        quantity = int(args[1])
        self.quantity = quantity
        self.slots_availability = [True] * quantity
        self.slots = [{}] * quantity
        print(f'Created a parking lot with {quantity} slots')

    def execute(self, parking_lot=None):
        pass