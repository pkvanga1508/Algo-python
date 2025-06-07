#Node Depths
# Problem: Given a binary tree, calculate the sum of the depths of all nodes.
# A node's depth is defined as the number of edges from the root to the node.
# The function should return the sum of the depths of all nodes in the tree.
# The function should have a time complexity of O(n) where n is the number of nodes in the tree.
# The function should have a space complexity of O(h) where h is the height of the tree.
def nodeDepths(root):
    # Write your code here.
    return node_depths(root, 0)

def node_depths(bst, curr_depth) :
    if bst is None:
        return 0

    return curr_depth + node_depths(bst.left, curr_depth + 1) + node_depths(bst.right, curr_depth + 1)



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
