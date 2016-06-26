
class GameRepository:

    def __init__(self):
        self.games = []

    def create_game(self, name):
        self.games.append(name)
        return len(self.games) - 1

    def load_game(self, id):
        return self.games[id]
