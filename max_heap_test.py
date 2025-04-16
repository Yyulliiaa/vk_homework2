import unittest
from max_heap import is_max_heap, is_max_heap_bfs

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right
def build_tree(array, i = 0):
    if i >= len(array):
        return None
    root = TreeNode(array[i])
    root.left = build_tree(array, 2 * i + 1)
    root.right = build_tree(array, 2 * i + 2)
    return root


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [21, 19, 18, 11, 12, 15, 16, 9, 8, 10]
        self.assertEqual(is_max_heap(arr), True)
    def test2(self):
        arr = [21, 19, 18, 48, 12, 15, 16, 9, 8, 10]
        self.assertEqual(is_max_heap(arr), False)
    def test3(self):
        arr = [21, 19, 18, 48, 12, 15, 16, 9, 8, 10]
        self.assertEqual(is_max_heap_bfs(build_tree(arr)), False)
    def test4(self):
        arr = [21, 19, 18, 11, 12, 15, 16, 9, 8, 10]
        self.assertEqual(is_max_heap_bfs(build_tree(arr)), True)


if __name__ == '__main__':
    unittest.main()
