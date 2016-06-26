from Game import character_repo

class Square:

    def __init__(self, x, y):
        self.x, self.y = x, y

class Map:

    def __init__(self, size = 5):
        self.map = []
        self.size = size
        for i in range(size):
            self.map.append([])
            for j in range(size):
                self.map[i-1].append(Square(i-1, j-1))

        self.unit_position = {}

    def add_unit(self, id, position):
        self.unit_position[id] = position

    def get_unit_position(self, id):
        return self.unit_position[id]

    def get_moveable_positions(self, id):
        print(character_repo.get_character_by_id(id))
        movement_range = character_repo.get_character_by_id(id).stats[0].movement
        current_x, current_y = self.get_unit_position(id)
        valid_squares = []
        occupied_squares = [self.unit_position[x] for x in self.unit_position]
        for i in range(self.size):
            for j in range(self.size):
                if [i,j] in occupied_squares:
                    continue
                if abs(i - current_x) > movement_range or abs(j - current_y) > movement_range:
                    continue
                valid_squares.append([i,j])
        return valid_squares

    def can_move(self, id, pos):

        try:
            self.map[pos[0]][pos[1]]
        except:
            return False

        return True

    def move(self, id, pos):
        if not self.can_move(id, pos):
            return False
        self.unit_position[id] = pos
        return True

    def to_json(self):
        return {"size": self.size, "unit_positions": self.unit_position}