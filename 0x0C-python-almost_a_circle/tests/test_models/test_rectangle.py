#!/usr/bin/python3
""" Unittest """
import unittest
import io
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test rectangle class """

    def test_00_id(self):
        """ Correct Case id: full args """
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_00_width(self):
        """ Correct case 'width': 2 args """
        self.assertEqual(Rectangle(2, 3).width, 2)

    def test_00_height(self):
        """ Correct case 'height': 2 args """
        self.assertEqual(Rectangle(4, 5).height, 5)

    def test_00_x(self):
        """ Correct case 'x': 2, 3 and 4 args """
        self.assertEqual(Rectangle(4, 6).x, 0)
        self.assertEqual(Rectangle(6, 3, 9).x, 9)
        self.assertEqual(Rectangle(9, 8, 7, 9).x, 7)

    def test_00_y(self):
        """ Correct case 'y': 2, 3 and 4 args """
        self.assertEqual(Rectangle(1, 2).y, 0)
        self.assertEqual(Rectangle(2, 6, 4).y, 0)
        self.assertEqual(Rectangle(2, 2, 3, 5).y, 5)

    def test_01_typeError_width(self):
        """ TypeError: variable 'width' """
        with self.assertRaises(TypeError):
            Rectangle('a', 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(False, 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(float("inf"), 2, 3, 4)

    def test_01_typeError_height(self):
        """ TypeError: variable 'height' """
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 'hello', 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, True, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, float("inf"), 3, 4)

    def test_01_typeError_x(self):
        """ TypeError: variable 'x' """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 'Holberton', 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 5.6, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, False, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, float("inf"), 4)

    def test_01_typeError_y(self):
        """ TypeError: variable 'y' """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, True)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 'Betty')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 9.8)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, float("inf"))

    def test_02_missing_args_width(self):
        """ Missing args: variable 'widht' """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_02_missing_args_height(self):
        """ Missing args: variable 'height' """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_03_valueError_width(self):
        """ ValueError: variable 'width' """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_03_valueError_height(self):
        """ ValueError: variable 'height' """
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_03_valueError_x(self):
        """ ValueError: variable 'x' """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_03_valueError_y(self):
        """ ValueError: variable 'y' """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_04_area(self):
        """ testing area """
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(5, 3, 0, 0, 30).area(), 15)

    def test_05_display(self):
        """ Testing display without 'x' and 'y' """
        r = Rectangle(1, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "#\n#\n#\n")

    def test_06_display(self):
        """ Testing display with 'x' and 'y' """
        r = Rectangle(1, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n\n  #\n  #\n  #\n")

    def test_07_print(self):
        """ function print rectangle with format """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        r2 = Rectangle(4, 5, 2, 3, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 2/3 - 4/5")

    def test_08_update_args_1(self):
        """ Update 'ID' """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3)
        self.assertEqual(r1.id, 3)

    def test_08_update_args_2(self):
        """ Update 'ID' and 'width' """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3, 2)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 2)

    def test_08_update_args_3(self):
        """ Update 'ID' and 'width' and 'height' """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3, 2, 4)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)

    def test_08_update_args_4(self):
        """ Update 'ID' and 'width' and 'height' and 'x' """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3, 2, 4, 5)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)

    def test_08_update_args_full(self):
        """ updating data with full args """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3, 2, 4, 5, 4)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (3) 5/4 - 2/4")

    def test_09_update_kwargs_id(self):
        """ Update k/v var 'id' """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89)
        self.assertEqual(r1.id, 89)

    def test_09_update_kwargs_width(self):
        """ Update k/v var 'width' """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=6)
        self.assertEqual(r1.width, 6)

    def test_09_update_kwargs_height(self):
        """ Update k/v var 'height' """
        r1 = Rectangle(6, 10, 10, 10)
        r1.update(height=7)
        self.assertEqual(r1.height, 7)

    def test_09_update_kwargs_x(self):
        """ Update k/v var 'x' """
        r1 = Rectangle(6, 7, 10, 10)
        r1.update(x=12)
        self.assertEqual(r1.x, 12)

    def test_09_update_kwargs_y(self):
        """ Update k/v var 'y' """
        r1 = Rectangle(6, 7, 12, 10)
        r1.update(y=24)
        self.assertEqual(r1.y, 24)


if __name__ == "__main__":
    unittest.main()
