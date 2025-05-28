## Given an array of n-2 numbers in the range of 1 to n, find the two missing numbers.
# The function should return a list containing the two missing numbers.
# The function should have a time complexity of O(n) and a space complexity of O(1).
# The function should not use any additional data structures.
#   # Example:
#   nums = [1, 2, 4, 6]
#   missingTwoNumbers(nums) should return [3, 5].

def missingTwoNumbers(nums):

    array_len = len(nums) + 2
    required_sum = (array_len * (array_len + 1)) // 2
    actual_sum = sum(nums)
    missing_sum = required_sum - actual_sum
    avg_missing_sum = missing_sum // 2
    required_left_sum = (avg_missing_sum * (avg_missing_sum + 1)) // 2
    requited_right_sum = sum(range(avg_missing_sum + 1, array_len + 1))
    actual_left_sum = 0
    actual_right_sum = 0
    for num in nums:
        if num <= avg_missing_sum:
            actual_left_sum += num
        else:
            actual_right_sum += num
    return [required_left_sum - actual_left_sum, requited_right_sum - actual_right_sum]

