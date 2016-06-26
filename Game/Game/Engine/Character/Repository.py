from .Character import Stats, CharacterInfo
import json
import os

class CharacterRepository:

    def __init__(self):
        self.characters = []
        for filey in os.listdir(r"C:\Users\j.coltman\Documents\GitHub\Heroclix\Game\Game\Engine\Character\Info"):
            with open(os.path.join(r"C:\Users\j.coltman\Documents\GitHub\Heroclix\Game\Game\Engine\Character\Info", filey)) as char_file:
                self.add_character_from_json(json.load(char_file))

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
        dials = list(map(parse_stats, json_stats))
        character = CharacterInfo(details["name"], [], dials)
        self.add_character(character)
        with open(r"C:\Users\j.coltman\Documents\GitHub\Heroclix\Game\Game\Engine\Character\Info\{0}.json".format(character.name.replace(" ", "_").lower()), "w") as new_char_file:
            json.dump(details, new_char_file)

