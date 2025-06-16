/**
 * You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
 *
 * Return the minimum number of CPU intervals required to complete all tasks.
 *
 * Example 1:
 *
 * Input: tasks = ["A","A","A","B","B","B"], n = 2
 *
 * Output: 8
 *
 * Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
 *
 * After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.
 *
 * Example 2:
 *
 * Input: tasks = ["A","C","A","B","D","B"], n = 1
 *
 * Output: 6
 *
 * Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
 *
 * With a cooling interval of 1, you can repeat a task after just one other task.
 *
 * Example 3:
 *
 * Input: tasks = ["A","A","A", "B","B","B"], n = 3
 *
 * Output: 10
 *
 * Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
 *
 * There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
 *
 * Constraints:
 *
 * 1 <= tasks.length <= 104
 * tasks[i] is an uppercase English letter.
 * 0 <= n <= 100
 */


class Solution {
    public int leastInterval(char[] tasks, int n) {

        Map<Character, Integer> freqMap = new HashMap<>();
        //Build Freq Map
        for (char ch: tasks) {
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }

        //Build max heap based on the freq
        Queue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        maxHeap.addAll(freqMap.values());

        //Process
        int time = 0;
        while(!maxHeap.isEmpty()) {
            List<Integer> tmp = new ArrayList<>(); //Temporarily storing freq values so we can reduce the freq by one
            for (int i = 0; i < n + 1; i++) {  //We need to poll from Heap interval times (n + 1)
                if(!maxHeap.isEmpty()) { //If Heap is not empty poll the value and add it to tmp
                    int freq = maxHeap.poll();
                    tmp.add(freq);  //Add frequencies to the tmp
                }
            }

            //Reduce the values of freq from tmp and add it back to heap if they are > 0
            for(int val: tmp) {
                if(val - 1 > 0) {
                    maxHeap.offer(val - 1);
                }
            }

            //At this time we need to check if heap is empty -> last set of tasks are out but when reducing the freq their freq became 0 and are not added back to Heap
            //heap not empty -> Add standard interval (n + 1) to the time

            time +=  maxHeap.isEmpty() ? tmp.size() : n + 1;
        }

        return time;
    }
}