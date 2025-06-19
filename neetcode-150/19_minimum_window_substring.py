class Solution(object):
    def minWindow(self, s, t):

        target_freq = {}
        string_freq = {}

        if len(s) == 0 or len(t) > len(s):
            return ""

        #Solution
        sol_length = float("inf")
        sol_left = -1
        sol_right = -1

        for char in t:
            target_freq[char] =  target_freq.get(char, 0) + 1

        left = 0
        right = 0
        while right < len(s) :
            right_char = s[right]
            if right_char in target_freq:
                string_freq[right_char] = string_freq.get(right_char, 0) + 1

            if self.is_frequency_match(string_freq, target_freq) :
                curr_len = right - left + 1
                if curr_len < sol_length:
                    sol_length = curr_len
                    sol_left = left
                    sol_right = right

                #While frequency is matching move left untill frequency does not match
                #Also update count if the freq match
                while self.is_frequency_match(string_freq, target_freq):
                    curr_len = right - left + 1
                    if curr_len < sol_length:
                        sol_length = curr_len
                        sol_left = left
                        sol_right = right
                    left_char = s[left]
                    if left_char in target_freq :
                        string_freq[left_char] = string_freq.get(left_char) - 1
                    left += 1
            right += 1

        return s[sol_left : sol_right + 1] if sol_left >= 0 else ""

    def is_frequency_match(self, string_freq, target_freq):
        for char in target_freq:
            if string_freq.get(char, 0) < target_freq[char]:
                return False
        return True



