import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '..', 'parking_lot')))

from src.create_parking_lot import CreateParkingLot

import unittest


class CreateParkingLotTest(unittest.TestCase):
    """test cases for creating a parking lot"""

    def setUp(self):
        """method for setting up the test fixture before exercising tests"""
        args = "create_parking_lot 6"
        self.parking_lot1 = CreateParkingLot(args.split())
        args = "create_parking_lot 7"
        self.parking_lot2 = CreateParkingLot(args.split())
        args = "create_parking_lot 3"
        self.parking_lot3 = CreateParkingLot(args.split())

    def test_create_parking_lot_quantity(self):
        """test for parking slots quantity"""
        assert self.parking_lot1.quantity == 6
        assert self.parking_lot2.quantity == 7
        assert self.parking_lot3.quantity == 3

    def test_create_parking_lot_slots_availability(self):
        """test for  slots availability"""
        assert self.parking_lot1.slots_availability == [True] * 6
        assert self.parking_lot2.slots_availability == [True] * 7
        assert self.parking_lot3.slots_availability == [True] * 3

    def test_slots_vehicle_details(self):
        """test for vehicle details"""
        assert self.parking_lot1.slots == [{}] * 6
        assert self.parking_lot2.slots == [{}] * 7
        assert self.parking_lot3.slots == [{}] * 3


