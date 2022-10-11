import unittest

from block_1.builtin_functions.task_1.implementation import (
    Value,
)
from block_1.common import (
    MyException,
)


class MyTestCase(unittest.TestCase):
    def test_on_addition(self):
        seven = Value(7)
        self.assertEqual(seven + 3, 10)
        self.assertEqual(seven + 4, 11)

    def test_on_subtraction(self):
        ten = Value(10)
        self.assertEqual(ten - 3, 7)
        self.assertEqual(ten - 10, 0)

    def test_on_multiplication(self):
        seven = Value(7)
        self.assertEqual(seven * 3, 21)
        self.assertEqual(seven * (-1), -7)
        self.assertEqual(seven * 0, 0)
        zero = Value(0)
        self.assertEqual(zero * 3, 0)

    def test_on_division(self):
        ten = Value(10)
        self.assertEqual(ten / 2, 5)
        self.assertEqual(ten / 4, 2.5)
        x = lambda: ten / 0
        self.assertRaises(MyException, x)


if __name__ == '__main__':
    unittest.main()
