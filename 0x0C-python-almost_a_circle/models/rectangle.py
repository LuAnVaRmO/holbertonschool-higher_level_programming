#!/usr/bin/python3
""" Module rectangle(base) """
from models.base import Base


class Rectangle(Base):
    """ Class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ getter height"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ getter y variable """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter y variable """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print rectangle with ## """
        for e in range(self.__y):
            print()
        for r in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ Print format rectangle """
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
             self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update values of rectangle """
        ord_att = ["id", "width", "height", "x", "y"]
        if args and args != ():
            for i in range(len(args)):
                setattr(self, ord_att[i], args[i])
        if kwargs:
            for key in kwargs:
                if hasattr(self, key):
                    setattr(self, key, kwargs[key])
