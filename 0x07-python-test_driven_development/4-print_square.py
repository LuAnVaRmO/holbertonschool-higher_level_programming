#!/usr/bin/python3
"""
print_square
This function print a square with #
return square
"""


def print_square(size):
    """
    :param size: integer, size of the length
    :return: square, size * size
    """
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        pass
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
