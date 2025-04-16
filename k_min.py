import unittest
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


def inorder_min_iterative(node, k):
    stack = []
    counter = 0
    current = node
    while len(stack) > 0 or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1
        if counter == k:
            return current.data
        current = current.right
    return None

def inorder_min(node, k, counter = 0):
    if node is None:
        return None
    left_res = inorder_min(node.left, k, counter)
    if left_res:
        return left_res
    counter += 1
    if counter == k:
        return node.data
    return inorder_min(node.right, k, counter)


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27]
        root = build_tree(arr)
        self.assertEqual(inorder_min_iterative(root, 1), 2)
    def test2(self):
        arr = [16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27]
        root = build_tree(arr)
        self.assertEqual(inorder_min(root, 1), 2)
    def test3(self):
        arr = [16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27]
        root = build_tree(arr)
        self.assertEqual(inorder_min_iterative(root, 4), 10)
    def test4(self):
        arr = [16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27]
        root = build_tree(arr)
        res = inorder_min(root, 4)
        self.assertEqual(res, 10)



if __name__ == '__main__':
    unittest.main()