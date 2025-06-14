# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    result = []
    def bfs(self, root, level):
        if not root:
            return

        if len(self.result) <= level:  #Create a new empty list for each level
            self.result.append([]) #Add empty list

        self.result[level].append(root.val)

        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []  # Reset result for each call
        self.bfs(root, 0)
        return self.result