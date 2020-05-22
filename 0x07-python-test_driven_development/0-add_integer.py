#!/usr/bin/python3
"""
add_integer
adds two numbers (int or float)
return int(a) + int(b)
"""


def add_integer(a, b=98):
    """
    :param a: int or float
    :param b: int or float
    :return: a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
