# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
#
# Input: root = [1,2]
# Output: 1
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height_of_node(root)
        return self.max_diameter

    def height_of_node(self, root):
        if not root:
            return 0

        left_height = self.height_of_node(root.left) #get left height
        right_height = self.height_of_node(root.right) #get right height
        self.max_diameter = max(self.max_diameter, left_height + right_height) #Updating the max_diameter if needed
        return 1 +  max(left_height, right_height) #This is diameter
