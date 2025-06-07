# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        if len(s) <= 1:
            return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == "[":
                stack.append(char)
            else:
                #Make sure stack is not empty.
                if len(stack) == 0:
                    return False
                if char == ')':
                    if stack[-1] != '(':
                        return False
                    stack.pop()
                elif char == '}':
                    if stack[-1] != '{':
                        return False
                    stack.pop()
                elif char == ']':
                    if stack[-1] != '[':
                        return False
                    stack.pop()
        return len(stack) == 0