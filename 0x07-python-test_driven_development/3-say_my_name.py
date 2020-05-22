#!/usr/bin/python3
"""
say_my_name
This function say my name, only if is a string
return my name is {first_name} {last name}
"""


def say_my_name(first_name, last_name=""):
    """
    :param first_name: string with name
    :param last_name: string with lastname
    :return: my name is {first_name} {last name}
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
