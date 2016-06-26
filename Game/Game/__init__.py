from .GameState import GameState
from .Character.Repository import CharacterRepository
import os
import json

character_repo = CharacterRepository()

if character_repo.characters == []:
    for filey in os.listdir("Character/Info"):
        with open(os.path.join("Character/Info", filey)) as char_file:
            character_repo.add_character_from_json(json.load(char_file))
state = GameState()