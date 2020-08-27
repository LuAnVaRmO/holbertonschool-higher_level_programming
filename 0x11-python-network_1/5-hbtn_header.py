#!/usr/bin/python3
""" Script to see the header of specific url """
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    page = res.headers.get("X-Request-Id")
    print(page)
