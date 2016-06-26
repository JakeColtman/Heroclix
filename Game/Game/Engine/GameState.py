

class GameState:

    def __init__(self):
        self.engine = None

    def get_engine(self):
        return self.engine

    def set_engine(self, engine):
        self.engine = engine