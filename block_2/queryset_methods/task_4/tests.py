from datetime import (
    date,
)

from block_2.queryset_methods.task_4.implementation import (
    get_top_product_by_total_count_in_period,
)
from block_2.queryset_methods.tests import (
    BaseTest,
)


class ModelTest(BaseTest):

    def test_january(self):
        self.assertEqual(get_top_product_by_total_count_in_period(date(2021, 1, 1), date(2021, 1, 31)), [('Молоко', 10)])

    def test_febraury(self):
        self.assertEqual(get_top_product_by_total_count_in_period(date(2021, 2, 1), date(2021, 2, 28)), [('Молоко', 4)])

    def test_march(self):
        self.assertEqual(get_top_product_by_total_count_in_period(date(2021, 3, 1), date(2021, 3, 31)), [('Молоко', 8)])

    def test_april(self):
        self.assertEqual(get_top_product_by_total_count_in_period(date(2021, 4, 1), date(2021, 4, 30)), [])