## Find the kth largest value in a Binary Search Tree (BST).
# Problem: Given a Binary Search Tree (BST) and an integer k, find the kth largest value in the BST.
# The function should return the kth largest value in the BST.
# The function should have a time complexity of O(h + k) where h is the height of the BST.
# The function should have a space complexity of O(h) where h is the height of the BST.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):

    stack = []
    curr = tree
    while curr is not None or len(stack) > 0 :
        while curr is not None:
            stack.append(curr)
            curr = curr.right #Reverse inorder
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.value
        curr = node.left #Reverse inorder
    return -1
