#!/usr/bin/python3
""" Class Rectangle inherits Base geometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        :return: area = b*h
        """
        return self.__width * self.__height

    def __str__(self):
        """ string Class to print function """
        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                   self.__height)
