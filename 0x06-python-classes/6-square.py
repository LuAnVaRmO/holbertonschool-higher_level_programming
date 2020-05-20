#!/usr/bin/python3
""" This module create a Square """


class Square:
    """ attribute private """

    def __init__(self, size=0, position=(0, 0)):
        """ Verifying type of value, size and position"""

        self.size = size
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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
    def position(self, value):
        """ set the position of the tuple """

        if isinstance(value, int) or len(value) != 2 or \
                isinstance(value[0], int) or isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

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
