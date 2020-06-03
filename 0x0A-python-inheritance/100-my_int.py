#!/usr/bin/python3
""" module My int rebel class """


class MyInt(int):
    """ MyInt class """
    def __ne__(self, value):
        return super().__eq__(value)

    def __eq__(self, value):
        return super().__ne__(value)
