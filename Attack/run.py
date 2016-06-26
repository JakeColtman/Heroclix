#!flask/bin/python
from flask import Flask, request, jsonify
import random
app = Flask(__name__)

def roll(num_dice):
    return sum([random.randint(1, 6) for x in range(num_dice)])

@app.route('/attack', methods = ["POST"])
def attack():
    details = request.get_json(silent = True)
    attack, defence, damage = details["attack"], details["defence"], details["damage"]
    totalAttack = attack + roll(2)
    if totalAttack >= defence:
        inflicted_damage = damage
    else:
        inflicted_damage = 0

    return jsonify({"final_damage":inflicted_damage, "die_value": totalAttack - attack})
if __name__ == '__main__':
    app.run(debug=True)