#!/usr/bin/python3
"""
lookup module
"""


def lookup(obj):
    """
    :param obj: object or class
    :return: list of attributes available
    """

    return dir(obj)
