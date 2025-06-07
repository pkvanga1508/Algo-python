# Invert a Binary Tree
# Problem: Given a binary tree, invert it so that the left and right children of all nodes are swapped.
# The function should return the root of the inverted tree.
# The function should have a time complexity of O(n) where n is the number of nodes in the tree.
# The function should have a space complexity of O(h) where h is the height of the tree.

def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return

    #Swap Left and Right Nodes
    tree.left, tree.right = tree.right, tree.left
    # process all the nodes
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
