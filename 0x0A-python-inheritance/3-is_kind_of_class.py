#!/usr/bin/python3
""" Verify with isinstance """


def is_kind_of_class(obj, a_class):
    """
    :param obj: object to analyze
    :param a_class: type of instance
    :return: True or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
