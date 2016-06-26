
class Player:

    def __init__(self, units):
        self.units = units

    def is_active(self):
        return any([x.can_act() for x in self.units])

    def active_units(self):
        return list(filter(lambda x: x.can_act(0), self.units))

    def does_own_unit(self, unit):
        return unit in self.units