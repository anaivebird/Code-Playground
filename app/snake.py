import json
import requests

def get_judge():
    with open('./checker/judge.cpp') as f:
        return f.read()
def get_run():
    with open('./checker/run.cpp') as f:
        return f.read()

def gen_output(data):
    data['judge'] = get_judge()
    print(data.keys())
    return_data = requests.post('http://192.168.245.129:5000/submit', json=data)
    return return_data.text