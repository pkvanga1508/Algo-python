## Validate Three Nodes in a Binary Search Tree
# Problem: Given three nodes in a Binary Search Tree (BST), determine if the second node is a direct descendent of the first node, and if the third node is a direct descendent of the second node.
# The function should return True if the conditions are met, and False otherwise.
# The function should have a time complexity of O(h) where h is the height of the BST.
# The function should have a space complexity of O(1).
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if is_descendent(nodeTwo, nodeOne):
        return is_descendent(nodeThree, nodeTwo)
    elif is_descendent(nodeTwo, nodeThree):
        return is_descendent(nodeOne, nodeTwo)
    else:
        return False

def is_descendent(node, target):
    if node is None:
        return False
    if node.value == target.value:
        return True
    if node.value > target.value:
        return is_descendent(node.left, target)
    else:
        return is_descendent(node.right, target)


