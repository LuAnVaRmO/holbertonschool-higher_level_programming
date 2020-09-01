#!/usr/bin/python3
"""Post an email address to the requested URL"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    try:
        req = post(argv[1], data={'email': argv[2]})
        print(req.text)
    except Exception as err:
        print(err)
