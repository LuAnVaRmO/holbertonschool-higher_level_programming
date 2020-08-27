#!/usr/bin/env python3
""" Script that display body of the response"""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':

    url = argv[1]
    val = {'email': argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
