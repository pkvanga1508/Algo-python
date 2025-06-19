class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            start_val = nums[start]
            mid_val = nums[mid]
            end_val = nums[end]
            if start_val > end_val:
                if start_val <= mid_val:  #No Value in between start and mid is solution as we already know start > end
                    start = mid + 1
                else:
                    end = mid #You cant ignore the fact that mid can be lowest value

            else: #start and end are in right positons
                return nums[start]

        return -1
