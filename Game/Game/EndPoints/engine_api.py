from flask import Blueprint, request, jsonify
from Game import game_state

engine_api = Blueprint('engine', __name__)

@engine_api.route('/engine/add_unit', methods = ["POST"])
def add_unit():
    details = request.get_json()
    character_id, x, y = details["character_id"], details["x"], details["y"]
    game_state.get_engine().map.add_unit(character_id, [x,y])
    return jsonify({"Status": "Sucess"})

@engine_api.route('/engine/end_turn', methods = ["POST"])
def end_turn():
    return jsonify({"current_turn_index": game_state.get_engine().end_turn()})