import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '..', 'parking_lot')))
sys.path.append(os.path.abspath(os.path.join('..', '..', 'parking_lot/src')))

from src.park import Park
from src.create_parking_lot import CreateParkingLot

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

    def test_check_slot_availability(self):
        """test for parking slots availability"""
        assert self.parking_lot.slots_availability[0] is False
        assert self.parking_lot.slots_availability[1] is False
        assert self.parking_lot.slots_availability[2] is False

    def test_vehicle_at_slot(self):
        """test for vehicle detail at a slot"""
        assert self.parking_lot.slots[0] == self.vehicle1
        assert self.parking_lot.slots[1] == self.vehicle2
        assert self.parking_lot.slots[2] == self.vehicle3




