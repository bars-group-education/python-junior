import unittest

from block_1.lambda_function.task_2.implementation import (
    res_list,
)


class MyTestCase(unittest.TestCase):
    def test_on_filter(self):
        self.assertEqual(res_list, [(2, 2), (4, 8)])


if __name__ == '__main__':
    unittest.main()
