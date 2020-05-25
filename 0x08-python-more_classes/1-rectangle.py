#!/usr/bin/python3
"""
Create Rectangle class
"""


class Rectangle():
    """
    :param: width: width of the rectangle
    :param: height: height of the rectangle
    :return: rectangle class
    """

    def __init__(self, width=0, height=0):
        """ Init function of my class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter function variable 'width' """
        return self.width

    @width.setter
    def width(self, value):
        """ Setter function variable 'width' """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter function variable 'height' """
        return self.height

    @height.setter
    def height(self, value):
        """ Setter function variable 'height' """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
