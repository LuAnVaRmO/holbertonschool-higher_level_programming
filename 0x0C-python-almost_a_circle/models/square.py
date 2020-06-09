#!/usr/bin/python3
""" Module square(rectangle) """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value <= 0:
            raise ValueError('size must be > 0')
        self.height = value
        self.width = value

    def __str__(self):
        """ Print format square """
        n = __class__.__name__
        i = self.id
        x = self.x
        y = self.y
        s = self.size
        return "[{}] ({}) {}/{} - {}".format(n, i, x, y, s)
