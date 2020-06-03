#!/usr/bin/python3
""" Module to return JSON representation """
import json


def to_json_string(my_obj):
    """
    :param my_obj: Object to read
    :return: JSON representation
    """
    return json.dumps(my_obj)
