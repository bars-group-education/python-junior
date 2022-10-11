from datetime import (
    date,
)

from block_2.queryset_methods.task_2.implementation import (
    get_top_customer_in_period,
)
from block_2.queryset_methods.tests import (
    BaseTest,
)


class ModelTest(BaseTest):

    def test_january(self):
        self.assertEqual(get_top_customer_in_period(date(2021, 1, 1), date(2021, 1, 31)), ('Иван', 2))

    def test_febraury(self):
        self.assertEqual(get_top_customer_in_period(date(2021, 2, 1), date(2021, 2, 28)), ('Олег', 1))

    def test_march(self):
        self.assertEqual(get_top_customer_in_period(date(2021, 3, 1), date(2021, 3, 31)), ('Павел', 1))

    def test_april(self):
        self.assertEqual(get_top_customer_in_period(date(2021, 4, 1), date(2021, 4, 30)), None)