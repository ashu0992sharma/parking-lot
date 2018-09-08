from create_parking_lot import ParkingLot
from park import Park
from leave import Leave
from status import Status
from slot_number_for_registration_number import SlotRegistrationNo
from no_command import NoCommand


def get_commands():
    commands = (Park, Leave, Status, SlotRegistrationNo)
    return {cls.name: cls for cls in commands}


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()

args = input()
# Find and execute the command
parking_lot = ParkingLot(args.split())

while True:
    args = input()
    # Find and execute the command
    command = parse_command(commands, args.split())
    command.execute(parking_lot)