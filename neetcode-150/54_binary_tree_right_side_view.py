# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    bfs_result = []
    def bfs(self, root, level):
        if not root:
            return
        if len(self.bfs_result) <= level:
            self.bfs_result.append([])

        self.bfs_result[level].append(root.val)

        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)

    def rightSideView_recursive(self, root: Optional[TreeNode]) -> List[int]:
        self.bfs_result = []
        self.bfs(root, 0)
        return [level[-1] for level in self.bfs_result]

    def rightSideView_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)
        while queue:
            level_size = len(queue)
            for size in range(level_size):
                node = queue.pop(0)
                if size == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result