class Solution(object):
    def maxSlidingWindow(self, nums, k):
        answer = []
        queue = []
        for index in range(len(nums)):

            #Remove all indexes in queue if they are out of window
            #Older indexes are towords the starting of the queue
            window_start = index - k + 1
            while len(queue) > 0 and queue[0] < window_start:
                queue.pop(0)

            curr_value = nums[index]

            #Remove all indexes in queue whose value < curr_value
            #All the lower values are at the end of queue as queue
            while len(queue) > 0 and nums[queue[-1]] < curr_value:
                queue.pop(-1)

            queue.append(index)

            if index >= k - 1:
                answer.append(nums[queue[0]])

        return answer
