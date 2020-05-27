#!/usr/bin/python3
"""
Class LockedClass
"""


class LockedClass:
    """Prevent new instances except 1"""
    __slots__ = ['first_name']
