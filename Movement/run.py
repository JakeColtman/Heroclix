#!flask/bin/python
from flask import Flask, jsonify, request
from Map import Map

app = Flask(__name__)


@app.route('/map/position/<int:unit_id>')
def index(unit_id):
    pos = map.get_unit_position(unit_id)
    return jsonify({"unit_id": unit_id, "position":pos})

if __name__ == '__main__':
    map = Map(5)
    map.add_unit(1, [1,1])
    map.add_unit(2, [3, 3])
    app.run(debug=True)
