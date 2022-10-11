from datetime import (
    date,
)
from decimal import (
    Decimal,
)

from block_2.queryset_methods.task_3.implementation import (
    get_top_order_by_sum_in_period,
)
from block_2.queryset_methods.tests import (
    BaseTest,
)


class ModelTest(BaseTest):

    def test_january(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 1, 1), date(2021, 1, 31)), ('4', Decimal(630)))

    def test_febraury(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 2, 1), date(2021, 2, 28)), ('6', Decimal(420)))

    def test_march(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 3, 1), date(2021, 3, 31)), ('7', Decimal(56)))

    def test_april(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 4, 1), date(2021, 4, 30)), None)