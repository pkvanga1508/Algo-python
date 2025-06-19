# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
#
# Input: nums = [1,0,1,2]
# Output: 3


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        num_set = set()
        for num in nums:
            num_set.add(num)
        max_count = 1
        curr_count = 1
        for num in num_set:
            if num - 1 in num_set: #value exist so ignore
                continue
            next_val = num + 1 #value does not exist so check all the values till they dont exist in map.
            while next_val in num_set:
                curr_count += 1
                next_val += 1
            if curr_count > max_count:
                max_count = curr_count
            curr_count = 1
        return max_count


