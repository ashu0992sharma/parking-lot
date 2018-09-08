from abs_parking import AbsParking


class Leave(AbsParking):
    """class to leave a particular parking slot"""
    name = "leave"

    def __init__(self, args):
        """
        constructor to leave a parking slot
        :param args: slot number to leave
        """
        self.slot = int(args[1])

    def execute(self, parking_lot=None):
        """excecuting leave command"""
        parking_lot.slots_availability[self.slot-1] = True
        parking_lot.slots[self.slot-1] = {}
        print(f"Slot number {self.slot} is free")