#!/usr/bin/python3
""" Module to return description """


def class_to_json(obj):
    """
    :param obj: is an instance of a Class
    :return: dictionary JSON
    """
    return obj.__dict__
