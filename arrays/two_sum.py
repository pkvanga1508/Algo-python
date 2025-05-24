# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# You may not use the same element twice.

def twoNumberSum(array, targetSum):

    result = []
    num_set = set() #Hashing
    for num in array:
        diff = targetSum - num
        if diff != num and diff in num_set:
            return [num, diff]
        else:
            num_set.add(num)

    return result

##############################################

def twoNumberSum_2(array, targetSum):

    num_set = set(array)
    for num in array:
        diff = targetSum - num
        if diff != num and diff in num_set:
            return [num, diff]
    # Write your code here.
    return []

###################################################

def twoNumberSum_3(array, targetSum):

    num_set = set(num for num in array) #Just a variation of creating new set
    for num in array:
        diff = targetSum - num
        if diff != num and diff in num_set:
            return [num, diff]
    # Write your code here.
    return []



