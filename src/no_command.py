from abs_parking import AbsParking

class NoCommand(AbsParking):
    def __init__(self, args):
        self._command = args[0]
        pass

    def execute(self, parking_lot=None):
        print('No command named %s' % self._command)
