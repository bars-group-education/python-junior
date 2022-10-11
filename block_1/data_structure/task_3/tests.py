import unittest

from block_1.data_structure.task_3.implementation import (
    copy_dict,
)


class MyTestCase(unittest.TestCase):

    def test_get_origin_dict_copy(self):
        inner_list = [1, 2, 3]
        inner_dict = {
            'key4': 4,
            'key5': inner_list,
        }
        origin_dict = {
            'key1': 1,
            'key2': 2,
            'key3': inner_dict,
        }

        result = copy_dict(origin_dict)

        inner_dict.update({
            'key4': 44,
            'key5': [55],
        })

        excepted_result = {
            'key1': 1,
            'key2': 2,
            'key3': {
                'key4': 4,
                'key5': [1, 2, 3],
            },
        }

        self.assertDictEqual(result, excepted_result)


if __name__ == '__main__':
    unittest.main()
