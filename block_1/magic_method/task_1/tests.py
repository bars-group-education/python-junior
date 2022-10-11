import unittest

from block_1.magic_method.task_1.implementation import (
    Hundred,
    Thousand,
    Million,
)


class MyTestCase(unittest.TestCase):
    def test_on_hundred(self):
        obj_value = Hundred(7)
        self.assertEqual(obj_value.get_value(), 700)

    def test_on_thousand(self):
        obj_value = Thousand(3)
        self.assertEqual(obj_value.get_value(), 3000)

    def test_on_million(self):
        obj_value = Million(1)
        self.assertEqual(obj_value.get_value(), 1000000)

    def test_on_arithmetic(self):
        obj_million = Million(1)
        obj_thousand = Thousand(1)
        obj_hundred = Hundred(1)
        res = obj_million - (obj_thousand * obj_hundred)
        self.assertEqual(res.get_value(), 900000)

    def test_on_all_arithmetic(self):
        a = Hundred(333)
        b = Thousand(44)
        c = Million(5)
        a += b * c
        c -= b / a
        res = a + b + c
        self.assertGreater(res.get_value(), 220005077299)


if __name__ == '__main__':
    unittest.main()
