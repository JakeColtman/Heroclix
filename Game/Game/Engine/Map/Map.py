

class Map:

    def __init__(self, width, height):
        self.blocking = [[-1,-1]]
        self.hindering = [[1,1]]
        self.width, self.height = width, height

    def is_valid_move(self, movement):
        pos = movement.ending_position

        failure = pos in self.blocking or pos[0] > self.width or pos[1] > self.height or pos[0] < 0 or pos[1] < 0
        return not failure

    def move(self, movement):
        return True

    def is_hindering(self, pos):
        return pos in self.hindering
