#!/usr/bin/python3
""" Class Student """


class Student:
    """ Class student """
    def __init__(self, first_name, last_name, age):
        """ Init method public attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        newdict = {}
        if type(attrs) != list:
            return self.__dict__
        for i in attrs:
            try:
                newdict[i] = self.__dict__[i]
            except:
                pass
        return newdict
