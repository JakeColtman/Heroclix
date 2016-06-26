from Engine import Engine

class GameRepository:

    def __init__(self):
        self.games = []

    def create_game(self, name):
        self.games.append(name)
        return len(self.games) - 1

    def load_game(self, id):
        return self.games[id]

    def create_game_from_json(self, json_game):
        game = Engine(json_game["name"], json_game["size"])
        return self.create_game(game)