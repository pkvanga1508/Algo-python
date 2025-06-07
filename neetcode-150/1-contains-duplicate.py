# Brute froce - o(n2)
# Sort - check with next array - o(n log n)
# Use Auxillary data structure

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
#
# Output: true
#
# Explanation:
#
# The element 1 occurs at the indices 0 and 3.
#
# Example 2:
#
# Input: nums = [1,2,3,4]
#
# Output: false
#
# Explanation:
#
# All elements are distinct.
# 
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
#
# Output: true


# class Solution(object):
#     def containsDuplicate(self, nums):
#         num_set = set()
#         for num in nums:
#             if num in num_set:
#                 return True
#             else:
#                 num_set.add(num)
#         return False

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set(nums)
        return len(nums) != len(num_set)

