import unittest

from block_1.comprehensions.task_1.implementation import (
    flatten_list,
)


class MyUnitTest(unittest.TestCase):

    def test_flatten_list(self):
        matrix = [
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
        ]

        flat = flatten_list(matrix)

        self.assertListEqual(flat, [0, 0, 0, 1, 1, 1, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
