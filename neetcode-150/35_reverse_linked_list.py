# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev #Point curr next to previous
            prev = curr #Move prev node forward
            #curr = curr.next  -> Move curr node ooops we forgot to store this value
            curr = tmp

        return prev