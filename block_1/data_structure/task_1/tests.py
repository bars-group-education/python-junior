import unittest

from block_1.data_structure.task_1.implementation import (
    Tuple,
)


class MyTestCase(unittest.TestCase):

    def test_get_element_by_index(self):
        user_tuple = Tuple(1, 2, 3)

        self.assertEqual(user_tuple[0], 1)

    def test_del_element(self):
        user_tuple = Tuple(1, 2, 3)

        try:
            del user_tuple[0]
            result = "success"
        except TypeError:
            result = TypeError

        self.assertEqual(result, TypeError)

    def test_change_element(self):
        user_tuple = Tuple(1, 2, 3)

        try:
            user_tuple[0] = 2
            result = "fail"
        except TypeError:
            result = "success"

        self.assertEqual(result, "success")

    def test_get_index_with_not_exist_element(self):
        user_tuple = Tuple(1, 2, 3)

        try:
            user_tuple.index(4)
            result = "fail"
        except ValueError:
            result = "success"

        self.assertEqual(result, "success")

    def test_get_index_by_element(self):
        user_tuple = Tuple(1, 2, 4, 3, 4)

        self.assertEqual(user_tuple.index(4), 2)

    def test_get_count_for_element(self):
        user_tuple = Tuple(1, 2, 3, 1, 3, 4, 4)

        self.assertEqual(user_tuple.count(4), 2)


if __name__ == '__main__':
    unittest.main()
