/**
 * Given an integer array nums and an integer k, return the kth largest element in the array.
 *
 * Note that it is the kth largest element in the sorted order, not the kth distinct element.
 *
 * Can you solve it without sorting?
 *
 * Example 1:
 *
 * Input: nums = [3,2,1,5,6,4], k = 2
 * Output: 5
 * Example 2:
 *
 * Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
 * Output: 4
 *
 *
 * Constraints:
 *
 * 1 <= k <= nums.length <= 105
 * -104 <= nums[i] <= 104
 */

class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> min_heap = new PriorityQueue<>(k, (a, b) -> a - b);
        for(int num: nums) {
            if (min_heap.size() < k) {
                min_heap.offer(num);
            } else {
                int min_element = min_heap.peek();
                if (min_element < num) {
                    min_heap.poll();
                    min_heap.offer(num);
                }
            }
        }
        return min_heap.peek();
    }
}