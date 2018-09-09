from src.abs_parking import AbsParking


class SlotCarColor(AbsParking):
    """class to leave a particular parking slot"""
    name = "slot_numbers_for_cars_with_colour"

    def __init__(self, args):
        """
        constructor to print the slot no for a registration no
        :param args: registration number
        """
        self.color = args[1]

    def execute(self, parking_lot=None):
        """executing slot_number_for_registration_number command"""
        slots= []
        for index, slot in enumerate(parking_lot.slots):
            if slot and slot['color'] == self.color:
                slots.append(str(index+1))

        print(", ".join(slots))

