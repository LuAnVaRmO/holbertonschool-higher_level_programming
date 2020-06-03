#!/usr/bin/python3
""" check that 'obj' be an instance and not subclass """


def inherits_from(obj, a_class):
    """
    :param obj: object to analize
    :param a_class: type of instance
    :return: True or False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
