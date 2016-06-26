
class CharacterRepository:

    def __init__(self):
        self.characters = []

    def add_character(self, character):
        character.id = len(self.characters) + 1
        self.characters.append(character)

    def get_character_by_id(self, id):
        return self.characters[id - 1]

