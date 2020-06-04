#!/usr/bin/python3
""" Module to return JSON representation """
import json


def from_json_string(my_str):
    """
    :param my_str: string to read
    :return: JSON representation
    """
    return json.loads(my_str)
