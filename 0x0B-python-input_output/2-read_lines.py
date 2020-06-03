#!/usr/bin/python3
""" Module to read nb_lines of file """


def read_lines(filename="", nb_lines=0):
    """
    :param filename: file to read
    :param nb_lines: lines to read
    :return: print the number of lines nb_lines
    """
    with open(filename, "r") as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        for line in range(nb_lines):
            print(f.readline(), end="")
