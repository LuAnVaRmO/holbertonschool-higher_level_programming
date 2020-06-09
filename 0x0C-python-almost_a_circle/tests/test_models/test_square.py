#!/usr/bin/python3
""" Unittest """
import unittest
import io
import contextlib
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Test Square class """

    def test_00_id(self):
        """ Correct Case id: full args """
        self.assertEqual(Square(4).size, 4)
        self.assertEqual(Square(2, 3, 4, 5).id, 5)

    def test_00_size(self):
        """ Correct case 'size': 1 arg """
        self.assertEqual(Square(2).size, 2)

    def test_00_x(self):
        """ Correct case 'x': 2 args """
        self.assertEqual(Square(4, 5).x, 5)

    def test_00_y(self):
        """ Correct case 'y': 2 and 3 args """
        self.assertEqual(Square(4, 6).y, 0)
        self.assertEqual(Square(6, 3, 9).y, 9)

    def test_01_typeError_size(self):
        """ TypeError: variable 'size' """
        with self.assertRaises(TypeError):
            Square('a', 2, 3, 4)
        with self.assertRaises(TypeError):
            Square(1.5, 2, 3, 4)
        with self.assertRaises(TypeError):
            Square(False, 2, 3, 4)
        with self.assertRaises(TypeError):
            Square(float("inf"), 2, 3, 4)

    def test_01_typeError_x(self):
        """ TypeError: variable 'x' """
        with self.assertRaises(TypeError):
            Square(1, 2.5, 3, 4)
        with self.assertRaises(TypeError):
            Square(1, 'hello', 3, 4)
        with self.assertRaises(TypeError):
            Square(1, True, 3, 4)
        with self.assertRaises(TypeError):
            Square(1, float("inf"), 3, 4)

    def test_01_typeError_y(self):
        """ TypeError: variable 'y' """
        with self.assertRaises(TypeError):
            Square(1, 2, 'Holberton', 4)
        with self.assertRaises(TypeError):
            Square(1, 2, 5.6, 4)
        with self.assertRaises(TypeError):
            Square(1, 2, False, 4)
        with self.assertRaises(TypeError):
            Square(1, 2, float("inf"), 4)

    def test_02_missing_args_width(self):
        """ Missing args: variable 'size' """
        with self.assertRaises(TypeError):
            Square()

    def test_03_valueError_size(self):
        """ ValueError: variable 'size' """
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0, 1)

    def test_03_valueError_x(self):
        """ ValueError: variable 'x' """
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_03_valueError_y(self):
        """ ValueError: variable 'y' """
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_04_area(self):
        """ testing square area """
        self.assertEqual(Square(3, 2, 3).area(), 9)
        self.assertEqual(Square(5, 3, 0).area(), 25)

    def test_05_display(self):
        """ Testing display square without 'x' and 'y' """
        r = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_06_display(self):
        """ Testing display square with 'x' and 'y' """
        r = Square(1, 3, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n\n   #\n")

    def test_07_print(self):
        """ function print square with format """
        r1 = Square(2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Square] (5) 3/4 - 2")
        r2 = Square(5, 2, 3, 1)
        self.assertEqual(r2.__str__(), "[Square] (1) 2/3 - 5")

    def test_08_dictionary(self):
        """ Dictionary representation rectangle """
        r1 = Square(2, 2, 1, 89)
        r1_dic = {'size': 2, 'x': 2, 'id': 89, 'y': 1}
        self.assertEqual(r1.to_dictionary(), r1_dic)


if __name__ == "__main__":
    unittest.main()
