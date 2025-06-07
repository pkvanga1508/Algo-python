# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        freq_array_s1 = [0] * 26
        freq_array_s2 = [0] * 26
        char_a = ord('a')
        for index in range(len(s1)):
            freq_array_s1[ord(s1[index]) - char_a] += 1
            freq_array_s2[ord(s2[index]) - char_a] += 1

        #Window
        start = 0
        end = len(s1) # start at len(s1) index
        while end < len(s2):
            if freq_array_s1 == freq_array_s2:
                return True
            freq_array_s2[ord(s2[end]) - char_a] += 1
            freq_array_s2[ord(s2[start]) - char_a] -= 1 #Remove frequency
            end += 1
            start += 1

        return freq_array_s1 == freq_array_s2 #Edge case scenario where end becomes len(s2) but we have not compared the freq map.



