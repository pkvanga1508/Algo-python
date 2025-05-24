# Problem: Given an array of positive integers representing coin denominations,
# return the minimum amount of change (the smallest integer) that cannot be
# created with the given coins.
# For example, if the coins are [1, 2, 5], the minimum amount of change that
# cannot be created is 4. If the coins are [5, 7, 1, 1, 2, 3, 22], the minimum
# amount of change that cannot be created is 4. If the coins are [1, 1, 1, 1],
# the minimum amount of change that cannot be created is 5. If the coins are
# [1, 2, 3], the minimum amount of change that cannot be created is 7. If the
# coins are [1, 2, 3, 4], the minimum amount of change that cannot be created
# is 8. If the coins are [1, 2, 3, 4, 5], the minimum amount of change that
# cannot be created is 16. If the coins are [1, 2, 3, 4, 5, 6], the minimum
# amount of change that cannot be created is 22. If the coins are [1, 2, 3, 4,
# 5, 6, 7], the minimum amount of change that cannot be created is 29.

def nonConstructibleChange(coins):
    coins = sorted(coins)  # Sort the coins in ascending order
    # Write your code here.
    max_change_that_can_be_made = 0

    for coin in coins:
        if max_change_that_can_be_made + 1 < coin:  # This means we can not make max_change_that_can_be_made + 1
            return max_change_that_can_be_made + 1
        max_change_that_can_be_made += coin

    return max_change_that_can_be_made + 1
