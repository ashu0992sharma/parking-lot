import abc


class AbsParking(metaclass=abc.ABCMeta):
    """Abstact class for Parking"""
    slots_availability = []
    slots = []
    name = ''


    @abc.abstractmethod
    def execute(self, parking_lot=None):
        pass