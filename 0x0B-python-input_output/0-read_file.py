#!/usr/bin/python3
""" Module to read file """


def read_file(filename=""):
    """
    :param filename: file
    :return: open and print all lines of file
    """
    with open(filename, 'r') as f:
        for i in f:
            print(i, end="")
