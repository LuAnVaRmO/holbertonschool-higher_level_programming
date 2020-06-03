#!/usr/bin/python3
""" Module to count lines """


def number_of_lines(filename=""):
    """
    :param filename: file to read
    :return: number of lines of the file
    """
    count = 0
    with open(filename, "r") as f:
        while f.readline() != '':
            count += 1
        return count
