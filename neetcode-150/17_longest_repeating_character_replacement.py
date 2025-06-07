# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 1
        start = 0
        end = 0
        char_count = [0] * 26
        char_a = ord('A')
        max_occurence = 0
        while end < len(s):
            curr_length = end - start + 1
            char_count[ord(s[end]) - char_a] += 1
            max_occurence = max(max_occurence, char_count[ord(s[end]) - char_a])
            if curr_length - max_occurence <= k:
                length = max(length, curr_length)
                end += 1
            else:
                char_count[ord(s[start]) - char_a] -= 1
                start += 1
        return length
