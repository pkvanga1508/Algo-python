/**
 * Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 * Example 2:
 *
 * Input: nums = [1], k = 1
 * Output: [1]
 *
 *
 * Constraints:
 *
 * 1 <= nums.length <= 105
 * -104 <= nums[i] <= 104
 * k is in the range [1, the number of unique elements in the array].
 * It is guaranteed that the answer is unique.
 *
 *
 * Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */

class TopKElements {
    public int[] topKFrequent(int[] nums, int k) {
        var freq_map = new HashMap<Integer, Integer>();
        for(int num : nums) {
            freq_map.put(num, freq_map.getOrDefault(num, 0) + 1);
        }
        var heap = new PriorityQueue<Integer>((a, b) -> freq_map.get(a) - freq_map.get(b));
        for(int key : freq_map.keySet()) {
            heap.add(key);
            if(heap.size() > k){
                heap.poll();
            }
        }
        int[] solution = new int[k];
        for (int i = 0; i < k; i++) {
            solution[i] = heap.poll();
        }
        return solution;
    }
}