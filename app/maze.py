import base64
from random import randint, choice
import string

import requests

from app.models import Submission


def gen_random_maze(n=50):
    o, m = randint(n // 2, n), randint(n // 2, n)
    p = []
    for i in range(o):
        p.append(''.join([choice('.*') for i in range(m)]))
    return '%d %d\n' % (o, m) + ''.join(map(lambda x: ''.join(x) + '\n', p))

def random_string(n):
    return ''.join([choice(string.ascii_lowercase) for i in range(n)])


def base64encode(binary):
    return base64.b64encode(binary).decode()


def base64decode(binary):
    return base64.b64decode(binary).decode()


def gen_output(pk, code, lang):
    inp = gen_random_maze()
    data = {
        "input": base64encode(inp.encode()),
        "max_time": 1,
        "max_memory": 128,
        "submission": {
            "lang": lang,
            "fingerprint": random_string(64),
            "code": code
        }
    }
    token = ('ejudge', 'naive')
    return_data = requests.post('http://123.57.161.63:5002/judge/output', json=data, auth=token).json()
    print(return_data)
    submission = Submission.objects.get(pk=pk)
    if return_data.get('status') == "received":
        submission.verdict = return_data.get('verdict', 0)
        submission.running_input = inp
        submission.running_result = base64decode(return_data.get('output', ''))
    else:
        submission.verdict = 1
    submission.save()
