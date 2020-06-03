#!/usr/bin/python3
""" verify if 'obj' isinstance of 'a_class' """


def is_same_class(obj, a_class):
    """
    :param obj: object to analize
    :param a_class: type to compare
    :return: True or false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
