import unittest
from datetime import (
    date,
)

from block_1.flow_control.task_4.implementation import (
    get_next_date,
)


class MyTestCase(unittest.TestCase):
    def test_next_day(self):
        self.assertEqual(get_next_date(date(2021, 3, 3)), date(2021, 3, 4))

    def test_next_month(self):
        self.assertEqual(get_next_date(date(2021, 4, 30)), date(2021, 5, 1))

    def test_next_year(self):
        self.assertEqual(get_next_date(date(2021, 12, 31)), date(2022, 1, 1))

    def test_next_extra_february(self):
        self.assertEqual(get_next_date(date(2020, 2, 28)), date(2020, 2, 29))


if __name__ == '__main__':
    unittest.main()
