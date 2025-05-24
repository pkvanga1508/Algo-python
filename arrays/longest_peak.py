# Given an array of integers, return the length of the longest peak.
# A peak is defined as a sequence of consecutive integers that are strictly increasing and then strictly decreasing.
# The peak must have at least three elements.
# The function should return the length of the longest peak in the array. If there are no peaks, return 0.
# The function should have a time complexity of O(n) and a space complexity of O(1).
# The function should not use any additional data structures.
def longestPeak(array):

    max_height = 0
    index = 1
    length = len(array)
    while index < length:
        curr_height = 1 #Reseting the height everytime
        if array[index] <= array[index - 1]: #Going down without going up
            index += 1
            continue
        while index < length and array[index] > array[index -1]: # Going up
            index += 1
            curr_height += 1
        if index == length or array[index] == array[index - 1]: # Flatline or reached end without going down
            continue
        while index < length and array[index] < array[index -1]: # Going down after going up
            index += 1
            curr_height += 1
        max_height = max(max_height, curr_height)
    return max_height