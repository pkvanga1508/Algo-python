# Given a list of seats represented as 0s (empty) and 1s (occupied), find the best seat index
# where the best seat is defined as the seat that maximizes the number of empty seats between it and the nearest occupied seats.
# The function should return the index of the best seat. If there are multiple best seats, return the one with the smallest index.
# The function should have a time complexity of O(n) and a space complexity of O(1).
# The function should not use any additional data structures.
## Example:
# seats = [1, 0, 0, 1, 0, 0, 0, 1]
# bestSeat(seats) should return 4, as it is the index of the best seat with the maximum number of empty seats (3) between it and the nearest occupied seats (1 at index 3 and 1 at index 7).

def bestSeat(seats):
    best_empty_seats = 0
    best_seat_index = -1
    start = 0
    end = 0
    while end < len(seats):
        if seats[start] == 1:
            start += 1
            end += 1
        elif seats[end] == 0:
            end += 1
        else:
            curr_empty_seats = end - start
            if curr_empty_seats > best_empty_seats:
                best_empty_seats = curr_empty_seats
                best_seat_index = (end + start - 1) // 2
            start = end

    return best_seat_index
