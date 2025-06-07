# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

class Solution(object):
    def groupAnagrams(self, strs):
        freq_map = {}
        for word in strs:
            freq_string = self.get_freq_string(word)
            print(freq_string)
            if freq_string in freq_map:
                freq_map[freq_string].append(word)
            else:
                freq_map[freq_string] = [word]
        return freq_map.values()

    def get_freq_string(self, word):
        freq_list = [0] * 26
        ord_a = ord('a')
        for letter in word:
            freq_list[ord(letter) - ord_a] += 1
            print(freq_list)
        return "".join(str(x) + "|" for x in freq_list)   # Appending "|" to fix an edge case where two words have same frequency (10 letters and 1,0 letters)
