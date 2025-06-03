# Given an array of positive integers, find the maximum sum of non-adjacent elements in the array.
# The function should return the maximum sum that can be obtained by selecting non-adjacent elements.
# The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.
# Max Subset Sum No Adjacent Problem.
# Given an array of positive integers, find the maximum sum of non-adjacent elements in the array.

def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    #max_array = [float("-inf") for _ in array]   #Initialize max_array with all -inf values
    max_array = array[:]  # Copy all the elemets as is.
    #max_array[0] = array[0]
    max_array[1] = max(array[0], array[1])
    for index in range(2, len(array)):
        max_array[index] = max(max_array[index - 1], array[index] + max_array[index - 2])
    return max_array[-1]

#####################################################################################################################

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for index in range(2, len(array)):
        curr_max = max(second, first + array[index])
        first = second
        second = curr_max
    # Write your code here.
    return max(first, second)

