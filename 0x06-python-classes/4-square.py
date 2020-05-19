#!/usr/bin/python3
""" This module create a Square """


class Square:
    """ attribute private """
    def __init__(self, size=0):
        """ Verifying type of value and size"""

        self.__size = size

    def area(self):
        """ Function area(size) """

        """ Function return size * size """
        return self.__size * self.__size

    @property
    def size(self):
        """ get the size of the square"""

        """Return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the value of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
