class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root == None:
        return []
    
    result = [root.value]

    if root.left != None:
        result.extend(pre_order_traversal(root.left))

    if root.right != None:
        result.extend(pre_order_traversal(root.right))

    return result


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

result = pre_order_traversal(root)
print(result)