# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
#
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
#
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for curr_index in range(len(temperatures)) :
            curr_temperature = temperatures[curr_index]
            if not stack :  #Stack empty
                stack.append(curr_index)
            else:
                #We have to do this exercise as long as curr_temperature > top of stack or stack is empty
                while stack and temperatures[stack[-1]] < curr_temperature: # We Found the hotter day for whatever is on top of stack
                    answer[stack[-1]] = curr_index - stack[-1] # Number of days to get to higher temperature
                    stack.pop()
                stack.append(curr_index)

        return answer
