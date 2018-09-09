from src.park import Park
from src.create_parking_lot import CreateParkingLot
from src.leave import Leave


import unittest


class ParkTest(unittest.TestCase):
    """test cases for parking a vehicle"""

    def setUp(self):
        """method for setting up the test fixture before exercising tests"""
        args = "create_parking_lot 6"
        self.parking_lot = CreateParkingLot(args.split())

        args = "park KA-01-HH-1234 White"
        self.park1 = Park(args.split())
        self.park1.execute(self.parking_lot)
        self.vehicle1 = {
                'registration_no': args.split()[1],
                'color': args.split()[2]
        }

        args = "park KA-01-HH-9999 White"
        self.park2 = Park(args.split())
        self.park2.execute(self.parking_lot)
        self.vehicle2 = {
            'registration_no': args.split()[1],
            'color': args.split()[2]
        }
        args = "park KA-01-BB-0001 Black"
        self.park3 = Park(args.split())
        self.park3.execute(self.parking_lot)
        self.vehicle3 = {
            'registration_no': args.split()[1],
            'color': args.split()[2]
        }

        args = "leave 3"
        self.leave1 = Leave(args.split())
        self.leave1.execute(self.parking_lot)

    def test_leave_slot(self):
        """test for parking slots availability"""
        assert self.parking_lot.slots_availability[0] is False
        assert self.parking_lot.slots_availability[1] is False
        assert self.parking_lot.slots_availability[2] is True





