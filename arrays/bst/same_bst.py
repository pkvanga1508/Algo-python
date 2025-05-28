# Same BSTs
# Write a function that takes in two arrays of integers and returns a boolean indicating whether the two arrays represent the same binary search tree (BST).
# The arrays are guaranteed to be non-empty and contain unique integers.
# The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the arrays.
# Same BSTs Problem.
def sameBsts(arrayOne, arrayTwo):

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False
    array_one_less_than_root = get_elements_less_than(arrayOne, arrayOne[0])
    array_two_less_than_root = get_elements_less_than(arrayTwo, arrayTwo[0])
    array_one_greater_equal_root = get_elements_greater_equal_than(arrayOne, arrayOne[0])
    array_two_greater_equal_root = get_elements_greater_equal_than(arrayTwo, arrayOne[0])

    return sameBsts(array_one_less_than_root, array_two_less_than_root) and sameBsts(array_one_greater_equal_root, array_two_greater_equal_root)

def get_elements_less_than(array, val):
    result = []
    for index in range(1, len(array)):
        if array[index] < val:
            result.append(array[index])
    return result

def get_elements_greater_equal_than(array, val):
    result = []
    for index in range(1, len(array)):
        if array[index] >= val:
            result.append(array[index])
    return result

##################################################################################################################################

# Example usage: