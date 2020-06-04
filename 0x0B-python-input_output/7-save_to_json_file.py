#!/usr/bin/python3
""" Module to write OBject to text file """
import json


def save_to_json_file(my_obj, filename):
    """
    :param my_obj: object to write
    :param filename: name of the file
    :return:
    """
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
