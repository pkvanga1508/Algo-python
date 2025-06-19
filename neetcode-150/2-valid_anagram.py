# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


#Python ascii equivalent - ord()
# lowercase chars only.
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq_list = [0] * 26
        ord_char_a = ord('a')
        for index in range(len(s)):
            freq_list[ord(s[index]) - ord_char_a] += 1
            freq_list[ord(t[index]) - ord_char_a] -= 1

        for val in freq_list:
            if val != 0:
                return False

        return True


