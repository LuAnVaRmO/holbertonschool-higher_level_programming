#!/usr/bin/python3
""" Module to add text """


def append_after(filename="", search_string="", new_string=""):
    """
    :param filename: name of file
    :param search_string: string to look for
    :param new_string: string to add in new line
    :return:
    """
    with open(filename, "r") as f:
        string = ""
        for i in f:
            string += i
            if search_string in i:
                string += new_string
    with open(filename, "w") as f:
        f.write(string)
