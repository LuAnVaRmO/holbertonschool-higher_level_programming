#!/usr/bin/python3
"""
Create Rectangle class
"""


class Rectangle:
    """
    :param: width: width of the rectangle
    :param: height: height of the rectangle
    :return: rectangle class
    """

    def __init__(self, width=0, height=0):
        """ Init function of my class"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Getter function variable 'height' """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter function variable 'height' """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Getter function variable 'width' """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function variable 'width' """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ return area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            per = 0
        else:
            per = 2 * (self.__width + self.__height)
        return per

    def __str__(self):
        """ Print te rectangle with # sign """
        if self.width == 0 or self.height == 0:
            return ""
        text = ""
        for i in range(self.__height):
            text += "#" * self.width
            text += '\n'
        text = text[:-1]
        return text

    def __repr__(self):
        """ representation to a square """
        text = "Rectangle({:s}, {:s})"
        return text.format(str(self.__width), str(self.__height))
