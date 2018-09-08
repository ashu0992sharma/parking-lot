import abc


class ParkingLot:
    """Parking Lot class to create a Parking lot"""
    name = 'create_parking_lot'
    slots_availability = []
    slots = []

    def __init__(self, args):
        """"""
        quantity = int(args[1])
        self.quantity = quantity
        self.slots_availability = [True] * quantity
        self.slots = [{}] * quantity
        print(f'Created a parking lot with {quantity} slots')

    @abc.abstractmethod
    def execute(self):
        pass