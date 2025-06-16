/**
 * The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
 *
 * For example, for arr = [2,3,4], the median is 3.
 * For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
 * Implement the MedianFinder class:
 *
 * MedianFinder() initializes the MedianFinder object.
 * void addNum(int num) adds the integer num from the data stream to the data structure.
 * double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 *
 *
 * Example 1:
 *
 * Input
 * ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
 * [[], [1], [2], [], [3], []]
 * Output
 * [null, null, null, 1.5, null, 2.0]
 *
 * Explanation
 * MedianFinder medianFinder = new MedianFinder();
 * medianFinder.addNum(1);    // arr = [1]
 * medianFinder.addNum(2);    // arr = [1, 2]
 * medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
 * medianFinder.addNum(3);    // arr[1, 2, 3]
 * medianFinder.findMedian(); // return 2.0
 *
 *
 * Constraints:
 *
 * -105 <= num <= 105
 * There will be at least one element in the data structure before calling findMedian.
 * At most 5 * 104 calls will be made to addNum and findMedian.
 *
 *
 * Follow up:
 *
 * If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
 * If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
 */




class MedianFinder {

    Queue<Integer> minHeap;
    Queue<Integer> maxHeap;

    public MedianFinder() {
        minHeap = new PriorityQueue<>((a,b) -> a - b);
        maxHeap = new PriorityQueue<>((a,b) -> b - a);
    }

    public void addNum(int num) {

        if(maxHeap.size() == 0) {
            maxHeap.offer(num);
            return;
        }

        if(minHeap.size() < maxHeap.size()) {
            //We want to insert in minHeap;
            if (num < maxHeap.peek()) {
                //num can not go in the min Heap
                //We poll the top element from max Heap and add num to min heap and polled elemet needs to be added to minHeap
                int tmp = maxHeap.poll();
                maxHeap.offer(num);
                minHeap.offer(tmp);
            } else {
                minHeap.offer(num);
            }
        } else {
            //We want to insert in maxHeap;
            if (num > minHeap.peek()) {
                //num can not go in the max Heap,
                //We poll the top element from min Heap and add num to min heap and polled elemet needs to be added to maxHeap
                int tmp = minHeap.poll();
                minHeap.offer(num);
                maxHeap.offer(tmp);
            } else {
                maxHeap.offer(num);
            }
        }
    }

    public double findMedian() {

        if (minHeap.size() < maxHeap.size()) {
            return maxHeap.peek();
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }

    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */