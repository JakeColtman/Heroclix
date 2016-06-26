#!flask/bin/python
from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

def roll(num_dice):
    return sum([random.randint(1, 6) for x in range(num_dice)])


if __name__ == '__main__':
    print(roll(1))
    #app.run(debug=True)