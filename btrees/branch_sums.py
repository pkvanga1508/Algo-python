## Given a binary tree, find the sum of all its branches.
# Problem: Given a binary tree, find the sum of all its branches.
# A branch is defined as a path from the root to any leaf node.
# The function should return a list of sums, where each sum corresponds to a branch in the tree.
# The function should have a time complexity of O(n) where n is the number of nodes in the tree.
# The function should have a space complexity of O(h) where h is the height of the tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    branch_sums_util(root, 0, result)
    return result

def branch_sums_util(bst, curr_sum, result):
    if bst is None:
        return
    curr_sum += bst.value
    if bst.left is None and bst.right is None:   #Root element
        result.append(curr_sum)
    branch_sums_util(bst.left, curr_sum, result)
    branch_sums_util(bst.right, curr_sum, result)



