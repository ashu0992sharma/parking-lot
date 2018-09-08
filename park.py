from create_parking_lot import ParkingLot
from constants import PARKING_FULL_ERROR


class Park:
    """Class to park a vehicle"""
    name = 'park'

    def __init__(self, args):
        """
        constructor to initializing park object
        :param args: 1. registration_no: registration_no of the vehicle
        2. color: color of the vehicle
        """
        self.registration_no = args[1]
        self.color = args[2]
        self.vehicle_detail = {
            'registration_no': self.registration_no,
            'color': self.color
        }

    def execute(self, parking_lot):
        """executing park command"""
        for index, slot in enumerate(parking_lot.slots_availability):
            if slot:
                parking_lot.slots_availability[index] = False
                parking_lot.slots[index] = self.vehicle_detail
                print(f"Allocated slot number: {index+1}")
                return
        print(PARKING_FULL_ERROR)


