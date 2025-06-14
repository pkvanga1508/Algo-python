# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
# Example 1:
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q: #Both p and q are None
            return True
        elif not p or not q: #We know both of them are not None and now checking if One of then is None
            return False
        elif p.val != q.val: #We know both are not None and one of them is not None -> both are not None
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)