import unittest

from block_1.lambda_function.task_1.implementation import (
    res_list,
)


class MyTestCase(unittest.TestCase):
    def test_on_hundred(self):
        self.assertEqual(res_list, [(6, 13), (4, 8), (55, 3), (2, 2)])

if __name__ == '__main__':
    unittest.main()
