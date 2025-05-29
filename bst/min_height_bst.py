#minHeight BST
# Problem: Given a sorted array, create a Binary Search Tree (BST) with minimal height.
# The function should return the root of the BST.

def minHeightBst(array):
    return min_height_bst_util(array, None, 0, len(array) -1)

#We are inserting one by one value
def min_height_bst_util(array, bst, start, end):
    if start <= end:
        mid = (start + end)//2
        node_val = array[mid]
        if bst == None:
            bst = BST(node_val)
        else:
            bst.insert(node_val)
        min_height_bst_util(array, bst, start, mid -1)
        min_height_bst_util(array, bst, mid + 1, end)
        return bst
    else:
        return None

############################################################################

def minHeightBst_2(array):
    return min_height_bst_util_2(array, None, 0, len(array) -1)

def min_height_bst_util_2(array, bst, start, end):
    if start <= end:
        return None
    mid = (start + end) // 2
    node_val = array[mid]
    bst = BST(node_val)  #Create the node with Value Here
    bst.left = min_height_bst_util_2(array, bst.left, start, mid -1) #Create Left Node
    bst.right = min_height_bst_util_2(array, bst.right, mid + 1, end) #Create Right Node
    return bst



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
