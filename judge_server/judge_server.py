from flask import Flask, request, abort, jsonify
import json
import sys
from subprocess import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


def getarr(lines):
    arr = []
    for line in lines:
        arr += line.split()
    return arr


@app.route('/submit', methods=['POST'])
def solve():
    dataDict = request.json
    if 'judge' in dataDict and 'run' in dataDict:
        with open('judge.cpp', 'w') as f:
            f.write(dataDict['judge'])
        with open('run.cpp', 'w') as f:
            f.write(dataDict['run'])
        p = Popen("python judge.py", shell=True)
        p.wait()
        data = dict()
        with open('./init', 'r') as f:
            data['init'] = getarr(f.readlines())

        with open('./food', 'r') as f:
            data['food'] = getarr(f.readlines())

        with open('./press', 'r') as f:
            data['press'] = f.readlines()
        return json.dumps(data)
    else:
        abort(403)


app.run('0.0.0.0', debug=True)

