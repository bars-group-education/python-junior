import unittest

from block_1.generators.task1.implementation import (
    fib,
)


class MyTestCase(unittest.TestCase):
    def test_fib_first_element(self):
        for num in fib(1):
            pass
        self.assertEqual(num, 1)

    def test_fib_third_element(self):
        for num in fib(3):
            pass
        self.assertEqual(num, 2)

    def test_fib_hundredth_element(self):
        for num in fib(100):
            pass
        self.assertEqual(num, 354224848179261915075)


if __name__ == '__main__':
    unittest.main()
