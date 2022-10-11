import unittest

from block_1.scope.task_4.implementation import (
    open_and_close_file,
)


class MyTestCase(unittest.TestCase):
    def test_open_and_close_file(self):
        self.assertEqual(open_and_close_file('description.md'), None)


if __name__ == '__main__':
    unittest.main()
