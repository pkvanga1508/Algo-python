# Problem: Given an array of integers and a target integer, write a function that moves all occurrences of the target integer to the end of the array.
# The function should return the modified array.
# The order of the other integers should be preserved.
# The function should have a time complexity of O(n) and a space complexity of O(1).
# The function should not use any additional data structures.
# Order is not preserved below.
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] != toMove:
            left += 1
        elif array[right] == toMove:
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return array


# Order is preserved below.
def moveElementToEnd_preserve_order(array, toMove):

    first = 0
    second = 1

    while first < len(array) and second < len(array):
        if array[first] != toMove:
            first += 1
            second = first + 1
        else:
            if array[second] == toMove:
                second += 1
            else: #Swap
                array[first], array[second] = array[second], array[first]
                first += 1
                second += 1
    # Write your code here.
    print(array)
    return array