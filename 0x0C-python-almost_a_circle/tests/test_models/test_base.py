#!/usr/bin/python3
""" Unittest """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test base task 1 """

    def test_correct(self):
        """  correct answer """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base('testing').id, 'testing')
        self.assertEqual(Base((1, 2)).id, (1, 2))
        self.assertEqual(Base(()).id, ())
        self.assertEqual(Base({'1': '2', '3': '4'}).id, {'1': '2', '3': '4'})
        self.assertEqual(Base('string' + ' concatenated').id, 'string concatenated')
        self.assertEqual(Base(True).id, True)
        self.assertEqual(Base(-98).id, -98)

    def test_wrong_cases(self):
        """ TypeErrors """
        with self.assertRaises(TypeError):
            Base(2, 'a')
        with self.assertRaises(TypeError):
            Base(1, 2)
