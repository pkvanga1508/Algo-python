def threeNumberSum(array, targetSum):
    
    result = []
    array = sorted(array)
    for pivot in range(len(array) - 2) :
        left = pivot + 1
        right = len(array)  - 1
        while left < right:
            print(len(array), pivot, left, right)
            curr_sum = array[pivot] + array[left] + array[right]
            if curr_sum == targetSum:
                result.append([array[pivot], array[left], array[right]])
                left += 1
                right -= 1
            elif curr_sum > targetSum:
                right -= 1
            else:
                left += 1
    return result
