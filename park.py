from create_parking_lot import ParkingLot
from constants import PARKING_FULL_ERROR


class Park(ParkingLot):
    """Class to park a vehicle"""
    name = 'park'

    def __init__(self, args):
        self.registration_no = args[1]
        self.color = args[2]
        self.vehicle_detail = {
            'registration_no': self.registration_no,
            'color': self.color
        }

    def execute(self):
        """executing park command"""
        import pdb;pdb.set_trace()
        for index, slot in enumerate(self.slots_availability):
            if slot:
                self.slots_availability[index] = False
                self.slots[index] = self.vehicle_detail
                return
        print(PARKING_FULL_ERROR)


