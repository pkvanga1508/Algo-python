# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_valid_bst_bfs(self, root, min, max):
        if not root:
            return True

        if root.val < min or root.val > max:
            return False

        return self.is_valid_bst_bfs(root.left, min, root.val - 1) and self.is_valid_bst_bfs(root.right, root.val + 1, max)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst_bfs(root, float("-inf"), float("inf"))