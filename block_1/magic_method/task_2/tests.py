import unittest

from block_1.magic_method.task_2.implementation import (
    MathClock,
)


class MyTestCase(unittest.TestCase):
    def test_on_zero_time(self):
        time_obj = MathClock()
        self.assertEqual(time_obj.get_time(), '00:00')

    def test_on_add_minutes(self):
        time_obj = MathClock()
        time_obj + 9
        self.assertEqual(time_obj.get_time(), '00:09')
        time_obj + 2
        self.assertEqual(time_obj.get_time(), '00:11')
        time_obj + 49
        self.assertEqual(time_obj.get_time(), '01:00')

    def test_on_add_hours(self):
        time_obj = MathClock()
        time_obj * 9
        self.assertEqual(time_obj.get_time(), '09:00')
        time_obj * 2
        self.assertEqual(time_obj.get_time(), '11:00')
        time_obj * 49
        self.assertEqual(time_obj.get_time(), '12:00')

    def test_on_hours_and_minutes(self):
        time_obj = MathClock()
        time_obj * 1
        time_obj + 61
        self.assertEqual(time_obj.get_time(), '02:01')


if __name__ == '__main__':
    unittest.main()
