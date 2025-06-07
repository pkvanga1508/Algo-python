## Longest Common Subsequence
# Given two strings, find the longest subsequence present in both of them.
# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
# The function should return the longest common subsequence as a list of characters.
def longestCommonSubsequence(str1, str2):
    memory = [[[] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for row in range(1, len(memory)):
        for col in range(1, len(memory[0])):
            if str1[row - 1] == str2[col - 1]:
                memory[row][col] =  memory[row - 1][col - 1] + [str1[row - 1]]
            else:
                largest_subproblem_string = memory[row - 1][col] if len(memory[row - 1][col]) > len(memory[row][col - 1]) else memory[row][col - 1]
                memory[row][col] = largest_subproblem_string
    return memory[-1][-1]