from pre_order_traversal import pre_order_traversal
from pre_order_traversal import BinaryTree
import unittest 

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        self.assertEqual(pre_order_traversal(root),[1, 2, 5, 3, 6, 7])
    

if __name__ == '__main__':
    unittest.main()