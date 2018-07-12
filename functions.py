import subprocess
import json
import os
import requests
import time

url = {
    'protocol': 'http://',
    'ip': 'localhost',  # 192.168.106.27
    'port': '8089',
    'live': '/live',
    'system': '/system'
}


def run_cmd(cmd):
    p = subprocess.Popen(cmd, universal_newlines=True, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    return p.stdout.read(), p.stderr.read()


def system(cmd):
    out, err = run_cmd(cmd)
    return json.loads(out)


def post_request(data, url):
    r = requests.post(url, data=json.dumps(data))
    print(r.status_code, r.reason)


def curr_time():
    return int(time.time())
