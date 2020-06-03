#!/usr/bin/python3
""" Module to write mode append a file """


def append_write(filename="", text=""):
    """
    :param filename: File to open mode append
    :param text: text to append
    :return: the total of new chars added
    """
    with open(filename,"a") as f:
        return f.write(text)
