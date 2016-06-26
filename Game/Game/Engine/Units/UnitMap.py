class UnitMap:

    def __init__(self, size = 5):
        max_x, max_y = size, size
        self.size = size
        self.units = {}

    def add_unit(self, id, position):
        self.units[id] = position

    def get_unit_position(self, id):
        return self.units[id]

    def is_valid_move(self, movement):
        pos = movement.ending_position
        unit_poses = [self.units[x] for x in self.units]
        print(unit_poses)
        success = pos not in unit_poses
        if not success:
            print("unit map")
        return success

    def move(self, movement):
        self.units[movement.unit.id] = movement.ending_position
        print(self.units[movement.unit.id])
        return True

    def to_json(self):
        return {"size": self.size, "unit_positions": self.units}