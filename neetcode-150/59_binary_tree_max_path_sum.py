# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
#
# Example 1:
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    max_sum = float("-inf")
    def max_gain(self, node):
        if not node:
            return 0

        left_gain = max(0, self.max_gain(node.left))
        right_gain = max(0, self.max_gain(node.right))
        new_path = node.val + left_gain + right_gain #This is just the path that is starting at node and goes left and right and ignoring the larger path
        self.max_sum = max(self.max_sum, new_path)
        return node.val + max(left_gain, right_gain)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_gain(root)
        return self.max_sum
