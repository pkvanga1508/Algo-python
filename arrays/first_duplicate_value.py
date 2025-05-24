# This is a sample code to find the first duplicate value in an array.
# Problem: Given an array of integers, find the first duplicate value that occurs more than once in the array.
# The function should return the first duplicate value that occurs more than once in the array.
# If there are no duplicate values, the function should return -1.
# The function should have a time complexity of O(n) and a space complexity of O(1).
# The function should not use any additional data structures.
def firstDuplicateValue(array):

    for val in array:
        index = abs(val) - 1
        if array[index] < 0 :
            return abs(val)
        else:
            array[index] *= -1
    # Write your code here.
    return -1
