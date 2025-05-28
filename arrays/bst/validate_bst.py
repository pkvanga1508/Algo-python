# Validate a Binary Search Tree (BST)
# Problem: Given a Binary Search Tree (BST), validate whether it is a valid BST.
# A valid BST is defined as a tree where for each node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value.
# The function should return True if the tree is a valid BST, and False otherwise.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstUtil(tree, float("-inf"), float("inf"))

def validateBstUtil(tree, min, max):
    if tree == None:
        return True
    if tree.value < min or tree.value > max:
        return False
    return validateBstUtil(tree.left, min, tree.value - 1) and validateBstUtil(tree.right, tree.value, max)
