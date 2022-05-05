# flask server for the solver
from flask import Flask, request
from solver import Solver
from trie import Trie, serializeTrie
import json

app = Flask(__name__)
solver = Solver()

@app.route('/solve', methods=['POST'])
def solve():
    boardString = request.form['board']
    return json.dumps(solver.solve(boardString), indent = 4)

@app.route('/reserialize', methods=['GET'])
def serialize():
    serializeTrie()
    solver = Solver()
    return "Done"

