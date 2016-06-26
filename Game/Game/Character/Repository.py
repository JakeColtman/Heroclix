from .Character import Stats, CharacterInfo
import json

class CharacterRepository:

    def __init__(self):
        self.characters = []

    def add_character(self, character):
        character.id = len(self.characters) + 1
        self.characters.append(character)

    def get_character_by_id(self, id):
        return self.characters[id - 1]

    def add_character_from_json(self, details):

        def parse_stats(json_stat):
            damage, attack, movement, defence = [json_stat[x] for x in ["damage", "attack", "movement", "defence"]]
            return Stats(movement, attack, defence, damage)

        json_stats = details["dials"]
        dials = map(parse_stats, json_stats)
        character = CharacterInfo(details["name"], [], dials)
        self.add_character(character)
        with open("Character/Info/{0}.json".format(character.name.replace(" ", "_").lower()), "w") as new_char_file:
            json.dump(details, new_char_file)

