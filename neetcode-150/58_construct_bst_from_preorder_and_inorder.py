#
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# Example 1:
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
# Constraints:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    preorder_index = 0
    inorder_index_map = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for index, val in enumerate(inorder):
            self.inorder_index_map[val] = index #Based on the inorder value we want to determine the index so we can use left [0 to Index-1] and right subtree [index + 1 to end] ranges

        return self.list_to_tree(preorder, 0, len(inorder) -1)


    def list_to_tree(self, preorder, left, right): #Left and Right indexes determine the left and right indexes from inorder traversal
        if left > right:
            return None
        root_val =  preorder[self.preorder_index]
        root = TreeNode(root_val) #Creating the root node
        self.preorder_index += 1
        root.left = self.list_to_tree(preorder,left, self.inorder_index_map[root_val] - 1)
        root.right = self.list_to_tree(preorder, self.inorder_index_map[root_val] + 1, right)
        return root