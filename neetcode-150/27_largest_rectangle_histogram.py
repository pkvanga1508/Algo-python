# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# Example 1:
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
# Constraints:
#
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0) #Takes care of incresing heights and we processed the whole list
        for curr_index in range(len(heights)) :
            if not stack:
                stack.append(curr_index)
            else:
                curr_height = heights[curr_index]
                #Height of top index is not valid anymore. Any value with height > curr_height is not valid in stack
                while len(stack) > 0 and heights[stack[-1]] > curr_height : # Also do this exercise for last index too
                    top = stack.pop()
                    height = heights[top]
                    #width = curr_index - top
                    #Cant just simply calculate width as curr_index - top
                    width = curr_index - stack[-1] -1 if len(stack) > 0 else curr_index
                    curr_area = width * height
                    if curr_area > max_area:
                        max_area = curr_area
                stack.append(curr_index)

        return max_area