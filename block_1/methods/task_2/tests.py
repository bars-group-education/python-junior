import unittest

from block_1.common import (
    MyException,
)
from block_1.methods.task_2.implementation import (
    ClassFather,
    User1,
    User2,
)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        ClassFather.registered_list.clear()

    def test_on_unregistered_child1(self):
        first_child = User1()
        self.assertRaises(MyException, first_child.get_name)

    def test_on_unregistered_child2(self):
        second_child = User2()
        self.assertRaises(MyException, second_child.get_name)

    def test_on_registered_child1(self):
        first_child = User1()
        first_child.register()
        self.assertEqual(first_child.get_name(), first_child._name)
        self.assertTrue(first_child.get_name())

    def test_on_registered_child2(self):
        second_child = User2()
        second_child.register()
        self.assertEqual(second_child.get_name(), second_child._name)
        self.assertTrue(second_child.get_name())

    def test_on_class_father(self):
        father = ClassFather()
        self.assertRaises(MyException, father.register)
        self.assertRaises(MyException, father.get_name)


if __name__ == '__main__':
    unittest.main()
