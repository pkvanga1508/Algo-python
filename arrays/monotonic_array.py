#Solution to Monotonic Array problem
# Problem: Given an array of integers, return true if the array is monotonic. An array is monotonic if it is either entirely non-increasing or non-decreasing.
# An array is non-increasing if its elements are in non-increasing order (i.e., each element is greater than or equal to the next element).
# An array is non-decreasing if its elements are in non-decreasing order (i.e., each element is less than or equal to the next element).
# The function should return true if the array is monotonic, and false otherwise.
def isMonotonic(array):
    if len(array) <= 1:
        return True
    is_incresing = array[-1] > array[0]
    for index in range(len(array) -1) :
        if (is_incresing and array[index] > array[index + 1]) or (not is_incresing and array[index] < array[index + 1]) :
            return False
    return True

################################################

def isMonotonic_2(array):

    is_decreasing = True
    is_increasing = True

    for index in range(1, len(array)):
        if array[index] > array[index - 1]:
            is_decreasing = False
        if array[index] < array[index - 1]:
            is_increasing = False
    return is_increasing or is_decreasing