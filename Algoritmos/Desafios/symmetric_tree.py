"""
Given a binary tree root, check if it's symmetric
around it's center (a mirror of itself).
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(3)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(4)
root.right.left = Node(5)

def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and \
               are_symmetric(root1.right, root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)

print(is_symmetric(root))