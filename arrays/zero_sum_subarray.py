## Function to check if there exists a subarray with a sum of zero
# Given an array of integers, return True if there exists a subarray (contiguous elements) with a sum of zero, otherwise return False.
# The function should have a time complexity of O(n) and a space complexity of O(n).
## The function should not use any additional data structures.
# This function uses a set to keep track of the cumulative sums seen so far.

def zeroSumSubarray(nums):

    sum_values = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in sum_values:
            return True
        else:
            sum_values.add(current_sum)
    return False