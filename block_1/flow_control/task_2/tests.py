import unittest

from block_1.flow_control.task_2.implementation import (
    convert_temperature,
)


class MyTestCase(unittest.TestCase):
    def test_get_zero_celsius(self):
        self.assertEqual(int(convert_temperature(0, 'F')), 32)

    def test_get_zero_fahrenheit(self):
        self.assertEqual(int(convert_temperature(0, 'C')), -17)

    def test_get_999_celsius(self):
        self.assertEqual(int(convert_temperature(999, 'F')), 1830)

    def test_get_999_fahrenheit(self):
        self.assertEqual(int(convert_temperature(999, 'C')), 537)

    def test_get_invalid_scale(self):
        self.assertEqual(int(convert_temperature(10, 'I')), 10)


if __name__ == '__main__':
    unittest.main()
