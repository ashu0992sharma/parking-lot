from create_parking_lot import ParkingLot
from park import Park
from no_command import NoCommand


def get_commands():
    commands = (ParkingLot, Park)
    return {cls.name: cls for cls in commands}


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()

while True:
    args = input()
    # Find and execute the command
    command = parse_command(commands, args.split())
    command.execute()