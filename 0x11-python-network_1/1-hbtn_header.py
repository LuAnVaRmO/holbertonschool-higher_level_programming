#!/usr/bin/python3
""" Script to see the header of specific url """
import urllib.request
from sys import argv


if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as res:
        print(res.info().get('X-Request-Id'))
