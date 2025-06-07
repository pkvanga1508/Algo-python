#levenshteinDistance
# Levenshtein distance is a measure of the difference between two sequences.
# It is defined as the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.
# The function should return the Levenshtein distance between the two input strings.
# The function should have a time complexity of O(m * n) where m and n are the lengths of the two strings.

def levenshteinDistance(str1, str2):
    memory = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    for index in range(len(memory)):
        memory[index][0] = index
    for index in range(len(memory[0])):
        memory[0][index] = index

    for row in range(1, len(memory)):
        for col in range(1, len(memory[0])):
            if str1[row - 1] == str2[col - 1]:
                memory[row][col] = min(memory[row -1][col - 1],
                                       memory[row - 1][col] + 1,
                                       memory[row][col - 1] + 1)
            else:
                memory[row][col] = min(memory[row -1][col - 1] + 1,
                                       memory[row - 1][col] + 1,
                                       memory[row][col - 1] + 1)
    return memory[-1][-1]
