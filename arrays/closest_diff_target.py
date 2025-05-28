## Given a list of dishes with their sweetness and savoriness levels, find the pair of dishes
# that have the closest sum to a target value. The dishes are represented as integers, where positive integers represent sweet dishes and negative integers represent savory dishes.
# The function should return a list containing the two dishes that have the closest sum to the target value.
# The function should have a time complexity of O(n log n) and a space complexity of O(1).

# Best Pair with Closest Sum to Target Problem.
def sweetAndSavory(dishes, target):
    if len(dishes) < 2 :
        return [0, 0]
    dishes = sorted(dishes)
    if dishes[0] > 0 or dishes[-1] < 0 :
        return [0, 0]
    start = 0
    end = len(dishes) - 1
    result = [0, 0]
    diff = float('inf')

    while dishes[start] < 0 and dishes[end] > 0:
        curr_target = dishes[start] + dishes[end]
        curr_diff = target - curr_target
        if curr_target <= target and curr_diff < diff:
            result = [dishes[start], dishes[end]]
            diff = curr_diff
        if curr_target == target:
            return result
        elif curr_target < target:
            start += 1
        else:
            end -= 1

    return result

