# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        front = None
        curr = head
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
            # front = curr.next
        return prev
                # /---------------------\
        # [data|.next] - > [data2|.next] -> [data3.next]