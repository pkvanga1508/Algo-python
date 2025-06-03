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
