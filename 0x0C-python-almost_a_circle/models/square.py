#!/usr/bin/python3
""" Module square(rectangle) """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Print formatted square """
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(i, x, y, s)

    def update(self, *args, **kwargs):
        """ Update values of square """
        ord_att = ["id", "size", "x", "y"]
        if args and args != ():
            for i in range(len(args)):
                setattr(self, ord_att[i], args[i])
        else:
            for key in kwargs:
                if hasattr(self, key):
                    setattr(self, key, kwargs[key])
