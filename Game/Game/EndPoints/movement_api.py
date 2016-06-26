#!flask/bin/python
from flask import jsonify, request
from Game import game_state
from flask import Blueprint

movement_api = Blueprint('map', __name__)

@movement_api.route('/game/map/position/<int:unit_id>')
def index(unit_id):
    pos = game_state.get_engine().map.get_unit_position(unit_id)
    return jsonify({"unit_id": unit_id, "position": pos})

@movement_api.route('/game/map/move/<int:unit_id>/x/<int:x>/y/<int:y>')
def move_unit(unit_id, x, y):
    game_state.get_engine().map.move(unit_id, [x, y])
    return jsonify({"unit_id": unit_id, "position": [x,y]})


@movement_api.route('/game/map/valid_moves/<int:unit_id>')
def valid_moves(unit_id):
    moves = game_state.get_engine().map.get_moveable_positions(unit_id)
    resp = {"unit_id": unit_id, "valid_moves": []}
    for move in moves:
        resp["valid_moves"].append({"x": move[0], "y": move[1],
                                    "url": "http://localhost:5000/map/move/{0}/x/{1}/y/{2}".format(unit_id, move[0],
                                                                                                   move[1])})

    return jsonify(resp)