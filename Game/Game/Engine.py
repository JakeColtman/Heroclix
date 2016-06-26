from Movement.Map import Map

class Engine:

    def __init__(self, name, map_size, teams):
        self.map = Map(map_size)
        self.name = name
        self.teams = teams
        self.current_turn_index = 0
        for team in self.teams:
            for unit in team.units:
                self.map.add_unit(unit["id"], unit["pos"])

    def to_json(self):
        map_json = self.map.to_json()
        return {
            "map": map_json,
            "name": self.name,
            "teams": self.teams
        }

    def end_turn(self):
        if self.current_turn_index < len(self.teams) - 1:
            self.current_turn_index += 1
        else:
            self.current_turn_index = 0
        return self.current_turn_index