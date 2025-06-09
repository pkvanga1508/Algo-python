
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) #We assume that len(nums1) is always <= len(nums2)

        start = 0
        end = len(nums1)
        while start <= end:
            num1split = (start + end) // 2 # We are moving the split on nums1 left or right based on start and end index
            num2split = ((len(nums1) + len(nums2) + 1) // 2) - num1split #Split is based on num1split

            num1left = nums1[num1split - 1] if num1split > 0 else float("-inf")
            num1right = nums1[num1split] if num1split < len(nums1) else float("inf")
            num2left = nums2[num2split - 1] if num2split > 0 else float("-inf")
            num2right = nums2[num2split] if num2split < len(nums2) else float("inf")

            if num1left <= num2right and num2left <= num1right:
                if (len(nums1) + len(nums2)) % 2 == 0: #Even
                    print(num1left, num2left, num1right, num2right)
                    return (max(num1left, num2left) + min(num1right, num2right)) / 2
                else:
                    return max(num1left, num2left)
            elif num1left > num2right :
                end = num1split - 1
            else:
                start = num1split + 1

        return 0









