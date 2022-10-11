import unittest

from block_1.lambda_function.task_4.implementation import (
    res_list_product,
    a,
)


class MyTestCase(unittest.TestCase):
    def test_on_filter(self):
        self.assertEqual(res_list_product, [a])


if __name__ == '__main__':
    unittest.main()
