#!/usr/bin/python3
""" Class to print a list sorted """


class MyList(list):
    """ Class to use with lists """

    def print_sorted(self):
        """
        :return: sorted list
        """
        print(sorted(self))
