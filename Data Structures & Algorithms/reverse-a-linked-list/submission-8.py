# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            # hold the next node
            hold = current.next
            # make the current node's next node the previous node
            current.next = prev
            # make the previous node the now current
            prev = current
            # current = hold
            current = hold
        return prev