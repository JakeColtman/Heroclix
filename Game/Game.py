from Movement.Map import Map

class Game:

    def __init__(self, name, map_size, teams = None):
        self.map = Map(map_size)
        self.name = name
        if teams is None:
            teams = []
        self.teams = teams

    def to_json(self):
        map_json = self.map.to_json()
        return {
            "map": map_json,
            "name": self.name,
            "teams": self.teams
        }