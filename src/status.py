from src.abs_parking import AbsParking


class Status(AbsParking):
    """class to leave a particular parking slot"""
    name = "status"

    def __init__(self, args):
        """
        constructor to print the status of parking lot
        :param args: slot number to leave
        """
        pass

    def execute(self, parking_lot=None):
        """executing leave command"""
        print("Slot No. Registration No Colour")
        for index, slot in enumerate(parking_lot.slots):
            if slot:
                print(f"{index+1}   {slot['registration_no']}   {slot['color']}")