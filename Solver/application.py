# flask server for the solver
from flask import Flask, request
from solver import Solver
from trie import serializeTrie
import json

application = Flask(__name__)
solver = Solver()

@application.route('/', methods=['GET'])
def hello():
    return "<p>This is an API for an iMessage word hunt solver. Use a POST to the /solve endpoint with a 'board' field formatted as 'abcdefghijklmnop' to return possible words</p>"

@application.route('/solve', methods=['GET','POST'])
def solve():
    if request.method == 'POST':
        boardString = request.form['board']
        return json.dumps(solver.solve(boardString), indent = 4)
    else:
        return "<p>Send this endpoint a post req</p>"

if __name__ == "__main__":
    application.run(threaded=True, port=5000)