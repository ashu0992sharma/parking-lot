from src.create_parking_lot import ParkingLot
from src.park import Park
from src.leave import Leave
from src.status import Status
from src.slot_number_for_registration_number import SlotRegistrationNo
from src.slot_numbers_for_cars_with_colour import SlotCarColor
from src.registration_numbers_for_cars_with_colour import RegistrationNoColor
from src.exit import Exit
from src.no_command import NoCommand


def get_commands():
    commands = (ParkingLot, Park, Leave, Status, SlotRegistrationNo, SlotCarColor, RegistrationNoColor, Exit)
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