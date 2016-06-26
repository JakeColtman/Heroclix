from Game.Engine.Units.Unit import Unit

class UnitFactory:

    def __init__(self, repo):
        self.max_id = 0
        self.repo = repo

    def create_character_by_id(self, id, position):
        info = self.repo.get_character_by_id(id)
        character = Unit(info.name, info.affiliations, info.stats)
        character.id = self.max_id
        character.position = position
        self.max_id += 1
        return character