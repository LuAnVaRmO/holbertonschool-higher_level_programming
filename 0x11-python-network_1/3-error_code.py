#!/usr/bin/python3
""" Script that display error msg """
import urllib.request
from sys import argv
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
        print(res.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
