# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        curr_max = 0
        trapped_water = 0
        for index in range(len(height)):
            lmax[index] = curr_max = max(curr_max, height[index])
        curr_max = 0
        for index in reversed(range(len(height))):
            rmax[index] = curr_max = max(curr_max, height[index])
        for index in range(len(height)):
            trapped_water += min(lmax[index], rmax[index]) - height[index]

        return trapped_water

    # More Optimized Solution.
    def trap2(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        lMax = 0
        rMax = 0
        water_trapped = 0
        while start < end:
            if height[start] < height[end]:  #Move to the end
                lMax = max(lMax, height[start])
                water_trapped += lMax - height[start]
                start += 1
            else:
                rMax = max(rMax, height[end])
                water_trapped += rMax - height[end]
                end -= 1
        return water_trapped