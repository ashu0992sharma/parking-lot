from create_parking_lot import ParkingLot
from park import Park
from leave import Leave
from status import Status
from slot_number_for_registration_number import SlotRegistrationNo
from slot_numbers_for_cars_with_colour import SlotCarColor
from no_command import NoCommand


def get_commands():
    commands = (ParkingLot, Park, Leave, Status, SlotRegistrationNo, SlotCarColor)
    return {cls.name: cls for cls in commands}


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()

while True:
    args = input()
    # Find and execute the command
    parking_lot = parse_command(commands, args.split())
    parking_lot.execute()

    while True:
        args = input()
        # Find and execute the command
        command = parse_command(commands, args.split())
        command.execute(parking_lot)