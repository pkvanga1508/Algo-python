class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return [0,0,0]

        result = []
        nums = sorted(nums)
        for index in range(len(nums) - 2):
            if index == 0 or nums[index] != nums[index - 1] :   #Avoid duplicates
                start = index + 1
                end = len(nums) - 1
                while start < end:
                    sum = nums[index] + nums[start] + nums[end]
                    if sum == 0:
                        print(index, start, end)
                        result.append([nums[index], nums[start], nums[end]])
                        start += 1
                        end -= 1
                    elif sum > 0:
                        end -= 1
                    else:
                        start += 1
        return result

