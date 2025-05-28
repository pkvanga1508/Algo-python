# This is the iterative solution to find the closest value in a BST
# Problem: Given a Binary Search Tree (BST) and a target value, find the closest value to the target in the BST.
# The function should return the closest value to the target in the BST.
# The function should have a time complexity of O(h) where h is the height of the BST.
# The function should have a space complexity of O(1).

def findClosestValueInBst(tree, target):
    closest = None
    closest_diff = float("inf")

    while tree != None:
        curr_diff = abs(tree.value - target)
        if curr_diff < closest_diff:
            closest_diff = curr_diff
            closest = tree.value
        if tree.value > target:
            tree = tree.left
        elif tree.value < target:
            tree = tree.right
        else:
            return tree.value
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#####################################################################

def findClosestValueInBstRecursion(tree, target):
    return find_closest_value_util(tree, target, tree.value)

def find_closest_value_util(tree, target, closest_value):
    if tree == None:
        return closest_value
    if abs(target - closest_value) > abs(target - tree.value): #Update the closest Value only if target is closer to current tree node
        closest_value = tree.value
    if tree.value > target:
        return find_closest_value_util(tree.left, target, closest_value)
    elif tree.value < target:
        return find_closest_value_util(tree.right, target, closest_value)
    else:
        return tree.value
