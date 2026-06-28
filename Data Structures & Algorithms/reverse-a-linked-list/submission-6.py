# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # understand
        # we are given the head of a linked list
        # return the opposite order of the nodes in a linkedlist
        # start at the head
        # hold the current value's next node
        # set the current node to previous node
        # make the previous 
        curr = head
        prev = None
        while curr:

            # [0]-> None
            heldnext = curr.next
            curr.next = prev
            # [0]-> None
            # maintain order of what the previous node is
            prev = curr
            curr = heldnext

        return prev