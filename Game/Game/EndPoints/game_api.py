#!flask/bin/python
from flask import Flask, jsonify, request
from character_api import character_api
from movement_api import movement_api
from engine_api import engine_api

from flask import Flask
from Game import game_repo, game_state
app = Flask(__name__)

app.register_blueprint(movement_api)
app.register_blueprint(character_api)
app.register_blueprint(engine_api)

@app.route("/game/load/<int:game_id>", methods=['GET'])
def load_game(game_id):
    engine = game_repo.load_game(game_id)
    game_state.set_engine(engine)
    return jsonify({"Status": "Success", "game_id": game_id})

@app.route("/game/create", methods=['POST'])
def create_game():
    details = request.get_json(silent = True)
    print(details)
    new_id = game_repo.create_game_from_json(details)
    load_game(new_id)
    response = jsonify({"Status": "Success", "game_id": new_id})
    return response


if __name__ == "__main__":
    app.run(debug=True)