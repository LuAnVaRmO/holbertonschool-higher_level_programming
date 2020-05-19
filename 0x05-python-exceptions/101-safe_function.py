#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
    return res
