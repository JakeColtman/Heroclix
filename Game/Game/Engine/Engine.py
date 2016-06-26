from Game.Engine.Map.Map import Map
from Game.Engine.Movement.MovementEngine import MovementEngine
from Game.Engine.Units.UnitMap import UnitMap

class Engine:

    def __init__(self, name, map_size, players):
        self.map = Map(map_size, map_size)
        self.name = name
        self.players = players
        self.current_turn_index = 0
        self.unit_map = UnitMap(map_size)
        for player in self.players:
            for unit in player.units:
                self.unit_map.add_unit(unit.id, unit.position)
        self.movement_engine = MovementEngine([self.map, self.unit_map])
        self.victory_state = "Not Started"

    def movement(self, movement):

        if not self.current_player().owns_unit(movement.unit):
            print("Current player doesn't own unit")
            return False

        if self.movement_engine.try_move(movement):
            movement.unit.actions_remaining -= 1
        else:
            return False

        if not self.current_player().is_active():
            self.end_turn()
        return True

    def current_player(self):
        return self.players[self.current_turn_index]

    def end_turn(self):
        print("ending turn")
        if self.current_turn_index < len(self.players) - 1:
            self.current_turn_index += 1
        else:
            self.current_turn_index = 0
        return self.current_turn_index