#!flask/bin/python
from flask import Flask, jsonify, request
from Repository import GameRepository

app = Flask(__name__)

@app.route("/game/create", methods=['POST'])
def create_game():
    details = request.get_json(silent = True)

    new_id = repo.create_game("Test")
    response = jsonify({"Status": "Success", "game_id": new_id})

    return response

@app.route("/game/load/<int:game_id>", methods=['GET'])
def load_game(game_id):
    return jsonify({"game_id": repo.load_game(game_id)})

if __name__ == '__main__':
    repo = GameRepository()
    app.run(debug=True)