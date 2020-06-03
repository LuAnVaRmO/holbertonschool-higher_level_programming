#!/usr/bin/python3
""" Class base geometry """


class BaseGeometry:
    """
    do nothing
    """
    def area(self):
        """
        :return: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        :param name: always string
        :param value: value to verify
        :return: nothing
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
