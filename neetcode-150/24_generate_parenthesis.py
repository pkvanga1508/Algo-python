# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
# Constraints:
#
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.backtrack(answer, "", 0, 0, n)
        return answer


    def backtrack(self, answer, curr_val, open, closed, max):
        if len(curr_val) == 2 * max:
            answer.append(curr_val)
            return

        if open < max: # we can add a open
            curr_val += '('
            self.backtrack(answer, curr_val, open + 1, closed, max)
            curr_val = curr_val[:-1] #Remove the last char 

        if closed < open: # we can add a close
            curr_val += ')'
            self.backtrack(answer, curr_val, open, closed + 1, max)
            curr_val = curr_val[:-1] #Remove the last char