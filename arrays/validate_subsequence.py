# This is a sample solution to the validate subsequence problem.
# Problem: Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
# A subsequence of an array is a new array that is formed from the original array by deleting some elements without changing the order of the remaining elements.
# For example, if the first array is [1, 2, 3, 4] and the second array is [1, 3], then the second array is a subsequence of the first one.
# The function should return True if the second array is a subsequence of the first one, and False otherwise.
# The function should have a time complexity of O(n) and a space complexity of O(1).
def isValidSubsequence(array, sequence):
    array_index = 0
    seq_index = 0
    while array_index < len(array) and seq_index < len(sequence):
        if array[array_index] == sequence[seq_index]:
            seq_index += 1
        array_index += 1

    return seq_index == len(sequence)

####################################################

def isValidSubsequence_2(array, sequence):

    seq_idx = 0
    for val in array:
        if seq_idx == len(sequence):
            return True
        if sequence[seq_idx] == val:
            seq_idx += 1
    # Write your code here.
    return seq_idx == len(sequence)
