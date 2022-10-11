import unittest

from block_1.common import (
    factorial,
    MyException,
)
from block_1.decorators.task_2.implementation import (
    check_value,
)


class MyTestCase(unittest.TestCase):
    def test_on_correct_values(self):
        new_factorial = check_value(factorial)
        self.assertEqual(new_factorial(5), 120)

    def test_on_str_value(self):
        new_factorial = check_value(factorial)
        self.assertRaises(MyException, new_factorial, '1')

    def test_on_none_value(self):
        new_factorial = check_value(factorial)
        self.assertRaises(MyException, new_factorial, None)

    def test_on_float_value(self):
        new_factorial = check_value(factorial)
        self.assertRaises(MyException, new_factorial, 7.5)

    def test_on_negative_value(self):
        new_factorial = check_value(factorial)
        self.assertRaises(MyException, new_factorial, -1)

    def test_on_zero_value(self):
        new_factorial = check_value(factorial)
        self.assertEqual(new_factorial(0), 1)


if __name__ == '__main__':
    unittest.main()
