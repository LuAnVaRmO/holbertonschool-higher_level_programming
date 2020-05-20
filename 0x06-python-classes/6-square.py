#!/usr/bin/python3
""" This module create a Square """


class Square:
    """ attribute private """

    def __init__(self, size=0, position=(0, 0)):
        """ Verifying type of value, size and position"""

        self.__size = size
        self.__position = position

    def area(self):
        """ Function area(size) """

        """ Function return size * size """
        return self.__size * self.__size

    @property
    def size(self):
        """ get the size of the square"""

        """ Return the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Function to show the position """

        """ Return the position """
        return self.__position

    @position.setter
    def position(self, position):
        """ set the position of the tuple """

        if type(position) is not int or len(position) != 2 or \
                type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """ Print a square with # """

        """ Function return the square painted with # """
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(' ', end='')
                else:
                    print('#', end='')
            print()
