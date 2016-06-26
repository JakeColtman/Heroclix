from Engine import Engine
from Team import Team


class GameRepository:

    def __init__(self):
        self.games = []

    def create_game(self, name):
        self.games.append(name)
        return len(self.games) - 1

    def load_game(self, id):
        return self.games[id]

    def create_game_from_json(self, json_game):
        teams = []
        for team in json_game["teams"]:
            teams.append(Team(team["name"], team["units"]))
        game = Engine(json_game["name"], json_game["size"], teams)
        return self.create_game(game)