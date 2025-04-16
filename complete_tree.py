import unittest


class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right


def is_complete_tree(root):
    if root is None:
        return True
    queue = [root]
    seen_none = False
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            seen_none = True
        else:
            if seen_none:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True



class MyTestCase(unittest.TestCase):
    def test1(self):
        root = TreeNode(8)
        root.right = TreeNode(3)
        root.left = TreeNode(9)
        root.left.right = TreeNode(11)
        root.left.left = TreeNode(6)
        self.assertEqual(is_complete_tree(root), True)
    def test2(self):
        root = TreeNode(8)
        root.right = TreeNode(3)
        root.left = TreeNode(9)
        root.right.left = TreeNode(6)
        self.assertEqual(is_complete_tree(root), False)

if __name__ == '__main__':
    unittest.main()