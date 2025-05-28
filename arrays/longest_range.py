#largest range in an array
# Problem: Given an array of integers, find the largest range of consecutive numbers that can be formed from the elements in the array.
# The function should return a list containing the start and end of the largest range.
# The function should have a time complexity of O(n) and a space complexity of O(n).
# This is a sample code to find the largest range in an array.
def largestRange(array):
    result = []
    max_range = 0
    visited_map = {}
    for num in array:
        visited_map[num] = False
    for num in array:
        if not visited_map[num]:
            range_start = num
            range_end = num + 1
            while range_start in visited_map:
                visited_map[range_start] = True
                range_start -= 1
            while range_end in visited_map:
                visited_map[range_end] = True
                range_end += 1
            curr_range = range_end - range_start - 2
            if curr_range >= max_range:
                max_range = curr_range
                result = [range_start + 1, range_end - 1]
                # Write your code here.
    return result
