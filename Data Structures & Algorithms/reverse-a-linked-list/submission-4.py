# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # head
        # iterate thjrough the list
        #   put list node in empty list
        #   hold next
        #   point current to previous 
        #   make next the previous so we can mocvce to the next pointer

        #  return head

        dummy = curr = head
        prev = None
        while curr:
            hold = curr

            holdnext = curr.next
            curr.next = prev
            prev = hold #which is current
            curr = holdnext

        return prev
