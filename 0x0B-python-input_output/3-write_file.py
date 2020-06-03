#!/usr/bin/python3
""" Module to write text on file """


def write_file(filename="", text=""):
    """
    :param filename: file to write
    :param text: string
    :return: new file or new text inside
    """
    with open(filename, "w") as f:
        return f.write(text)
