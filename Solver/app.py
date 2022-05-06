# flask server for the solver
from flask import Flask, request
from solver import Solver
from trie import serializeTrie
import json

app = Flask(__name__)
solver = Solver()

@app.route('/', methods=['GET'])
def hello():
    return "<p>This is an API for an iMessage word hunt solver. Use a POST to the /solve endpoint with a 'board' field formatted as 'abcdefghijklmnop' to return possible words</p>"

@app.route('/solve', methods=['POST'])
def solve():
    boardString = request.form['board']
    return json.dumps(solver.solve(boardString), indent = 4)

@app.route('/reserialize', methods=['GET'])
def serialize():
    serializeTrie()
    solver = Solver()
    return "Done"

if __name__ == "__main__":
    app.run(threaded=True, port=5000)