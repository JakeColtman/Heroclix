#!flask/bin/python
from flask import Flask, jsonify, request
from Character import CharacterInfo, Stats
import json
from Repository import CharacterRepository
import os
import requests

app = Flask(__name__)


@app.route('/character/list')
def list_characters():
    def process_character(character):
        return {"id": character.id, "details_url": "http://localhost:5000/character/details/{0}".format(character.id),
                "name": character.name}

    return jsonify({"characters": [process_character(x) for x in repo.characters]})


@app.route('/character/details/<int:character_id>')
def get_character_details(character_id):
    character = repo.get_character_by_id(character_id)
    return json.dumps(character.get_json())

@app.route("/character/create", methods=['POST'])
def create_character():
    details = request.get_json(silent = True)
    try:
        repo.add_character_from_json(request.get_json())
        response = jsonify({"Status": "Success"})
    except:
        response = jsonify({"Status": "Failure"})

    return response

if __name__ == '__main__':

    repo = CharacterRepository()

    if repo.characters == []:
        for filey in os.listdir("Info"):
            with open(os.path.join("Info", filey)) as char_file:
                repo.add_character_from_json(json.load(char_file))

    app.run(debug=True)
