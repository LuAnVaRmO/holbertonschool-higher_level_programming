#!/usr/bin/python3
""" Module to create an object """
import json


def load_from_json_file(filename):
    """
    :param filename: file to load
    :return:
    """
    with open(filename, "r") as f:
        return json.load(f)
