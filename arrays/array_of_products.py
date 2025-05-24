# Problem: Given an array of integers, return an array of the same length where each element at index i is equal to the product of all the numbers in the original array except the one at i.
# You must solve it without using division and in O(n) time complexity.
# The problem can be solved using two auxiliary arrays to store the products of the elements to the left and right of each index.
# The final result can be obtained by multiplying the corresponding elements of the left and right product arrays.
# The space complexity of this solution is O(n) because we are using two additional arrays of the same size as the input array.
# The time complexity is O(n) because we are iterating through the input array three times: once to fill the left product array, once to fill the right product array, and once to fill the result array.
# The function should return an array of the same length as the input array, where each element at index i is equal to the product of all the numbers in the original array except the one at i.
# The function should not use division and should have a time complexity of O(n) and a space complexity of O(n).
def arrayOfProducts(array):
    # Write your code here.
    left_product = [1 for _ in array]
    right_product = [1 for _ in array]
    result = [1 for _ in array]
    for index in range (1, len(array)):
        left_product[index] = left_product[index - 1] * array[index - 1]

    for index in range (len(array) - 2, -1 , -1):
        right_product[index] = right_product[index + 1] * array[index + 1]

    for index in range(len(array)):
        result[index] = left_product[index] * right_product[index]

    return result

##########################################################
#Optimised Algorithm + Approach
def arrayOfProducts_2(array):
    left_product = [1 for _ in array]
    product = [1 for _ in array]

    for index in range(1, len(array)):
        left_product[index] =  left_product[index -1] * array[index -1]

    right_product = 1
    for index in reversed(range(len(array))):
        product[index] = left_product[index] * right_product
        right_product *= array[index]

    # Write your code here.
    return product
