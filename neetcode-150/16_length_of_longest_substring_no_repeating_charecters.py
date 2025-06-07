# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1 :
            return len(s)

        length = 1
        start = 0
        end = 0
        char_set = set()
        while end < len(s):
            if s[end] not in char_set: #Keep incrementing and end ptr till duplicate char
                char_set.add(s[end])
                length = max(length, end - start + 1)
                end += 1
            else:
                char_set.remove(s[start]) #keep removing untill the duplicate char is removed
                start += 1
        return length
