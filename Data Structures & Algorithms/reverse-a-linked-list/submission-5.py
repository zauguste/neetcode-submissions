# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # notes:
        # create a previous pointer to hold the previous elements to make the current next the previous node
        # we want to hold the current next so that when we move to the next node we can after altering current's next to be previous
        # move to the next node using hold


# holdNext = current.next  1,2,3,None
# current.next = prev None, 1,2
# prev = current 3
# current = holdNext None

# prev starts at None                           |.next
        #       0 -> None 1 -> 0 2 -> 1 3 -> 2 None
        #None   
        #                               |     |   
        #                        prev     current
        prev = None
        curr = head
        holdNext = None
        while curr:
            holdNext = curr.next
            curr.next = prev
            prev = curr
            curr = holdNext
        return prev