# Given a binary tree, determine if it is height-balanced.
#
# Example 1:
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#
# Input: root = []
# Output: true
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left_height = self.height_node(root.left)
        right_height = self.height_node(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def height_node(self, root):
        if not root:
            return 0
        left_height = self.height_node(root.left)
        right_height = self.height_node(root.right)
        return 1 + max(left_height, right_height)

