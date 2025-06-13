# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        second = head

        for _ in range(n):             #Move the Second ptr till n places
            second = second.next

        if second is None:             #Size of the LL is same as N and you need to remove first element
            head = head.next
            return head

        while second.next is not None: #Move both First and Second ptrs
            first = first.next
            second = second.next

        if n > 1:
            tmp = first.next.next
            first.next = tmp
        else:
            first.next = None

        return head