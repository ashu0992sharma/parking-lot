from src.abs_parking import AbsParking


class SlotRegistrationNo(AbsParking):
    """class to leave a particular parking slot"""
    name = "slot_number_for_registration_number"

    def __init__(self, args):
        """
        constructor to print the slot no for a registration no
        :param args: registration number
        """
        self.registration_no = args[1]

    def execute(self, parking_lot=None):
        """executing slot_number_for_registration_number command"""

        for index, slot in enumerate(parking_lot.slots):
            if slot and slot['registration_no'] == self.registration_no:
                print(index+1)
                return
        print("Not found")
