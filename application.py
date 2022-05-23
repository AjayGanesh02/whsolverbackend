# flask server for the solver
from flask import Flask, request
from flask_cors import CORS
from solver import Solver
import json
import os

application = Flask(__name__)
CORS(application)
solver = Solver()

@application.route('/', methods=['GET'])
def hello():
    return "<p>This is an API for an iMessage word hunt solver. Use a GET to the /solve endpoint with a 'board' field formatted as 'abcdefghijklmnop' to return possible words</p>"

@application.route('/solve')
def solve():
    boardString = request.args.get('board')
    return json.dumps({"data" : solver.solve(boardString.lower())}, indent = 4)

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))