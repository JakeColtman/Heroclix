#!flask/bin/python
from flask import Flask, jsonify, request
import json
from Game import character_repo
from flask import Blueprint

character_api = Blueprint('character', __name__)

@character_api.route('/character/list')
def list_characters():
    def process_character(character):
        return {"id": character.id, "details_url": "http://localhost:5000/character/details/{0}".format(character.id),
                "name": character.name}

    return jsonify({"characters": [process_character(x) for x in character_repo.characters]})


@character_api.route('/character/details/<int:character_id>')
def get_character_details(character_id):
    character = character_repo.get_character_by_id(character_id)
    return json.dumps(character.get_json())

@character_api.route("/character/create", methods=['POST'])
def create_character():
    try:
        character_repo.add_character_from_json(request.get_json())
        response = jsonify({"Status": "Success"})
    except:
        response = jsonify({"Status": "Failure"})

    return response
