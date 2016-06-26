class Square:

    def __init__(self, x, y):
        self.x, self.y = x, y

class Map:

    def __init__(self, size = 5):
        self.map = []
        for i in range(size):
            self.map.append([])
            for j in range(size):
                self.map[i-1].append(Square(i-1, j-1))

        self.unit_position = {}

    def add_unit(self, id, position):
        self.unit_position[id] = position

    def get_unit_position(self, id):
        return self.unit_position[id]

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