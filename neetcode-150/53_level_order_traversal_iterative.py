# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)
        #There is a way to ignore this None - below impl
        queue.append(None) #Indicating one level is complete
        curr_level = []
        while len(queue) > 0: #Loop Till queue is empty
            node = queue.pop(0)
            if node:
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left) #add left child
                if node.right:
                    queue.append(node.right)
            else: #We hit None -> End of one level
                result.append([_ for _ in curr_level]) #Deep Copy
                curr_level = [] #Reset the curr_level
                if len(queue) > 0:
                    queue.append(None) #Indicating one level is complete

        return result

    def levelOrder_no_none_insert(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = []
        queue.append(root)
        while len(queue) > 0: #Loop Till queue is empty
            curr_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left) #add left child
                if node.right:
                    queue.append(node.right)

            result.append(curr_level) #Add current level to result
        return result