

class API:

    def __init__(self, engine, player):
        self.engine = engine
        self.player = player

    def get_api(self):
        if self.engine.players[self.engine.current_turn_index] != self.player:
            return {}
        else:
            return {
                "movement": [],
                "attack": []
            }