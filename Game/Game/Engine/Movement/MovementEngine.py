from Game.Engine.Movement.Movement import Movement

def generate_next_positions(position):
    possible_next_places = []
    for delta_x in [-1, 0, +1]:
        for delta_y in [-1, 0, 1]:
            possible_next_places.append([position[0] + delta_x, position[1] + delta_y])

    return possible_next_places

def pos_to_string( pos):
    return str(pos[0]) + "-" + str(pos[1])

class MovementEngine:
    def __init__(self, maps):
        self.maps = maps

    def is_valid_move(self, movement):
        return all([x.is_valid_move(movement) for x in self.maps])

    def try_move(self, movement):
        if not self.is_valid_move(movement):
            print("not a valid move")
            return False
        success = [x.move(movement) for x in self.maps]
        movement.unit.position = movement.ending_position
        return success

    def list_valid_movements(self, unit, start_position):
        try:
            movement_range = unit.get_stats().movement
        except:
            movement_range = 2
        considerations = {}

        def explore(current_pos, consideration, remaining_movement):
            if remaining_movement == 0:
                return consideration
            remaining_movement -= 1
            places = []
            for possible_next_step in generate_next_positions(current_pos):

                if pos_to_string(possible_next_step) not in consideration or consideration[
                    pos_to_string(possible_next_step)] < remaining_movement:


                    consideration[pos_to_string(possible_next_step)] = remaining_movement
                    places.append(explore(possible_next_step, consideration, remaining_movement))
            total_places = []
            for place in places:
                for p in place:
                    if p not in total_places:
                        total_places.append(Movement(unit, p))
            return total_places

        return explore(start_position, considerations, movement_range)
