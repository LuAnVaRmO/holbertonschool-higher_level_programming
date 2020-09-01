#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    r = requests.post(argv[1], data=value)
    print(r.text)
