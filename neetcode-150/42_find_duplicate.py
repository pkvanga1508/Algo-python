
#Solution where we can modify input array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            else:
                nums[index] *= -1

        return -1

    def findDuplicate_no_array_modification(self, nums: List[int]) -> int:
        #Slow and fast start a 0th index, slow moves 1 node and fast moves 2
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow: #Slow moves one place and fast moves two places
            slow = nums[slow]
            fast = nums[nums[fast]]

        #Reset slow to 0th index
        slow = 0

        #SLow and fast moves one Node at a time till they both meet
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast





