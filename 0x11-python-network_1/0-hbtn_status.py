#!/usr/bin/python3
""" Script that fetches a url """

import urllib.request


if __name__ == "__main__":
    r = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(r) as res:
        page = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode("utf-8")))
