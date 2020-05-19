#!/usr/bin/python3
""" This module create a Square """


class Square:
    """ attribute private """
    def __init__(self, size=0):
        """ Verifying type of value and size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
