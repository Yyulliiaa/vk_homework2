import unittest
from subtree import is_subtree
from build_tree import build_tree as bt


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        self.assertEqual(is_subtree(bt(arr), bt(arr)), True)  # add assertion here
    def test2(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        arr1 = [8, 9, 11, 7, 16, 3, 2]
        self.assertEqual(is_subtree(bt(arr), bt(arr1)), False)
    def test3(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        arr1 = []
        self.assertEqual(is_subtree(bt(arr), bt(arr1)), True)
    def test4(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        arr1 = [9, 7, 16]
        self.assertEqual(is_subtree(bt(arr), bt(arr1)), True)
    def test5(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        arr1 = []
        self.assertEqual(is_subtree(bt(arr1), bt(arr)), False)

if __name__ == '__main__':
    unittest.main()
