#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test using import Unittest
    """
    def test(self):
        """ Testing a correct output"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -5, -10]), -1)

    def test_empty(self):
        """ Testing a empty argument """
        self.assertEqual(max_integer(), None)

    def test_string(self):
        """ Testing string no integer """
        self.assertEqual(max_integer("edcba"), "e")

    def test_float(self):
        """ Testing only floats """
        self.assertEqual(max_integer([2.5, 3.2, 4.5, 4.8]), 4.8)

