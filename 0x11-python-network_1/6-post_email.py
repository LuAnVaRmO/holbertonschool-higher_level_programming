#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    val = {}
    val['email'] = email
    req = requests.post(url, val)
    print(req.text)
