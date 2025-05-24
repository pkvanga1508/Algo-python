# Merge Intervals
# Given a collection of intervals, merge any overlapping intervals.
# For example, given the intervals [[1,3],[2,6],[8,10],[15,18]], you should return [[1,6],[8,10],[15,18]].
#   # Example 1:
#   # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   # Output: [[1,6],[8,10],[15,18]]
#   # Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#   # Example 2:
#   # Input: intervals = [[1,4],[4,5]]
#   # Output: [[1,5]]

def mergeOverlappingIntervals(intervals):

    if len(intervals) <= 1:
        return intervals

    intervals = sorted(intervals, key = lambda interval : interval[0])
    result = []
    curr_interval = intervals[0]
    for next_interval in intervals:
        curr_interval_end = curr_interval[1]
        next_interval_start, next_interval_end = next_interval

        if curr_interval_end >= next_interval_start:
            curr_interval[1] = max(curr_interval_end, next_interval_end)
        else:
            result.append(curr_interval)
            curr_interval = next_interval

    result.append(curr_interval)  #Last one that is left over

    return result
