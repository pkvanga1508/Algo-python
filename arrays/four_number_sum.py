def fourNumberSum(array, targetSum):

    if len(array) < 4:
        return []
    array = sorted(array)
    result = []
    for first in range(len(array) - 3):
        second = first + 1
        for second in range(second, len(array) - 2):
            third = second + 1
            fourth = len(array) - 1
            while third < fourth:
                sum = array[first] + array[second] + array[third] + array[fourth]
                if sum == targetSum:
                    result.append([array[first], array[second], array[third], array[fourth]])
                    third += 1
                    fourth -= 1
                elif sum > targetSum:
                    fourth -= 1
                else:
                    third += 1
    return result
