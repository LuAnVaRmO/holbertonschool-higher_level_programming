#!/usr/bin/python3
""" Add attribute if its possible """


def add_attribute(obj, att, val):
    """ add attribute """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
