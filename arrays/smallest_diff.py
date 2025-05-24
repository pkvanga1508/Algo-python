# Given two arrays of integers, return an array containing the pair of numbers (one from each array) that have the smallest absolute difference. If there are multiple pairs with the same smallest difference, return any one of them.
# The absolute difference between two numbers is the absolute value of their difference.
# The function should have a time complexity of O(n log n) and a space complexity of O(1).
# The function should return a list containing the two numbers that have the smallest absolute difference.
# The input arrays may contain negative numbers, and the output array should also contain negative numbers if necessary.
# The input arrays may contain duplicate numbers, and the output array should also contain duplicate numbers if necessary.
# The input arrays may contain zero, and the output array should also contain zero if necessary.
def smallestDifference(arrayOne, arrayTwo):

    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    result = []
    smallest_diff = float('inf')
    ptr_one = 0
    ptr_two = 0

    while ptr_one < len(arrayOne) and ptr_two < len(arrayTwo) :
        curr_diff = abs(arrayOne[ptr_one] - arrayTwo[ptr_two])
        if curr_diff < smallest_diff:
            smallest_diff = curr_diff
            result = [arrayOne[ptr_one], arrayTwo[ptr_two]]
        if arrayOne[ptr_one] < arrayTwo[ptr_two]:
            ptr_one += 1
        else:
            ptr_two += 1

    return result
