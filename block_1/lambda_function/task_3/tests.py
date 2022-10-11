import unittest

from block_1.lambda_function.task_3.implementation import (
    res_list,
)


class MyTestCase(unittest.TestCase):
    def test_on_filter(self):
        self.assertEqual(res_list, [1, 4, 9])

if __name__ == '__main__':
    unittest.main()
