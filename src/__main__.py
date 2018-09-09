from create_parking_lot import CreateParkingLot
from park import Park
from leave import Leave
from status import Status
from slot_number_for_registration_number import SlotRegistrationNo
from slot_numbers_for_cars_with_colour import SlotCarColor
from registration_numbers_for_cars_with_colour import RegistrationNoColor
from exit import Exit
from no_command import NoCommand
import constants

import sys
import os


sys.path.append(os.path.abspath(os.path.join('..', '..', 'parking_lot')))


def get_commands():
    commands = (CreateParkingLot, Park, Leave, Status,
                SlotRegistrationNo, SlotCarColor,
                RegistrationNoColor, Exit)
    return {cls.name: cls for cls in commands}


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()

if len(sys.argv) < 2:
    # inputs from shell prompt
    args = input()
    # Find and execute the command
    parking_lot = parse_command(commands, args.split())
    while not isinstance(parking_lot, CreateParkingLot):
        print("Please create a parking_lot by create_parking_lot command")
        args = input()
        parking_lot = parse_command(commands, args.split())
    parking_lot.execute()

    while True:
        args = input()
        # Find and execute the command
        command = parse_command(commands, args.split())
        command.execute(parking_lot)
else:
    # running inputs from a file
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, constants.FUNCTIONAL_SPEC, constants.FIXTURES, sys.argv[1])
    with open(file_path) as input_file:
        args = input_file.readline().strip()
        parking_lot = parse_command(commands, args.split())
        parking_lot.execute()
        for line in input_file:
            args = line.strip()
            command = parse_command(commands, args.split())
            command.execute(parking_lot)

