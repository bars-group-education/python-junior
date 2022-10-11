import unittest

from block_1.flow_control.task_3.implementation import (
    get_days_count_by_month,
)


class MyTestCase(unittest.TestCase):
    def test_january(self):
        self.assertEqual(get_days_count_by_month('январь'), 31)

    def test_february(self):
        self.assertIn(get_days_count_by_month('февраль'), (28, 29))

    def test_march(self):
        self.assertEqual(get_days_count_by_month('март'), 31)

    def test_april(self):
        self.assertEqual(get_days_count_by_month('апрель'), 30)

    def test_may(self):
        self.assertEqual(get_days_count_by_month('май'), 31)

    def test_june(self):
        self.assertEqual(get_days_count_by_month('июнь'), 30)

    def test_july(self):
        self.assertEqual(get_days_count_by_month('июль'), 31)

    def test_august(self):
        self.assertEqual(get_days_count_by_month('август'), 31)

    def test_september(self):
        self.assertEqual(get_days_count_by_month('сентябрь'), 30)

    def test_october(self):
        self.assertEqual(get_days_count_by_month('октябрь'), 31)

    def test_november(self):
        self.assertEqual(get_days_count_by_month('ноябрь'), 30)

    def test_december(self):
        self.assertEqual(get_days_count_by_month('декабрь'), 31)

    def test_invalid(self):
        self.assertEqual(get_days_count_by_month('отдыхабрь'), 0)


if __name__ == '__main__':
    unittest.main()
