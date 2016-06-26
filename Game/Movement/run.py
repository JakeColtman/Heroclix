#!flask/bin/python
from flask import Flask, jsonify, request
from Map import Map

app = Flask(__name__)


@app.route('/game/map/position/<int:unit_id>')
def index(unit_id):
    pos = map.get_unit_position(unit_id)
    return jsonify({"unit_id": unit_id, "position": pos})


@app.route('/game/map/move/<int:unit_id>/x/<int:x>/y/<int:y>')
def move_unit(unit_id, x, y):
    map.move(unit_id, [x, y])
    return jsonify({"unit_id": unit_id, "position": [x,y]})


@app.route('/game/map/valid_moves/<int:unit_id>')
def valid_moves(unit_id):
    moves = map.get_moveable_positions(unit_id)
    resp = {"unit_id": unit_id, "valid_moves": []}
    for move in moves:
        resp["valid_moves"].append({"x": move[0], "y": move[1],
                                    "url": "http://localhost:5000/map/move/{0}/x/{1}/y/{2}".format(unit_id, move[0],
                                                                                                   move[1])})

    return jsonify(resp)


if __name__ == '__main__':
    map = Map(5)
    map.add_unit(1, [1, 1])
    map.add_unit(2, [3, 3])
    app.run(debug=True)
