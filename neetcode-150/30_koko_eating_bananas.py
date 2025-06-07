class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_size = max(piles) # Koko can eat maximum at this pace
        start = 1
        end = max_size #Need to decide on a number between start and end in which koko can take h hours to finish eating
        while start <= end:
            mid = (start + end) // 2
            hours = self.hours_to_finish(piles, mid, h)
            if hours > h: #Increase Pace
                start = mid + 1
            else:  #Decrease Pace
                end = mid - 1
        return start #Return the start as start is the lowest value in the range.


    def hours_to_finish(self, piles, pace, h):
        hours = 0
        for pile in piles:
            hours += ceil(pile/pace)
        return hours