# Given a sorted array of integers, write a function that returns a new array
# containing the squares of those integers also sorted in ascending order.
# The input array should be sorted in ascending order, and the output array
# should also be sorted in ascending order. The function should return a new
# array containing the squares of the integers in the input array, sorted in
# ascending order. The input array should not be modified.
# The function should have a time complexity of O(n) and a space complexity of O(n).

def sortedSquaredArray(array):

    start = 0
    end = len(array) - 1
    result = [0 for _ in array]
    result_index = len(result) - 1

    while start <= end:
        if abs(array[start]) > abs(array[end]):
            result[result_index] = array[start] * array[start]
            start += 1
        else:
            result[result_index] = array[end] * array[end]
            end -= 1

        result_index -= 1


        # Write your code here.
    return result

################################################

def sortedSquaredArray(array):

    start_idx = 0
    end_idx = len(array) - 1
    result = [0 for _ in array] #Fill everything with 0

    for idx in reversed(range(len(array))):  #Go from end to begining
        if abs(array[start_idx]) > abs(array[end_idx]) :
            result[idx] = array[start_idx] * array[start_idx]
            start_idx += 1
        else:
            result[idx] = array[end_idx] * array[end_idx]
            end_idx -= 1
            # Write your code here.
    return result
