# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Input: head = [0,1,2,3]
        #prevNode = None 0 prevNode<-cur.next| 1 prevNode<-cur.next 2 |prevNode <-cur.next 3 |prevNode <-cur.next
        # this must point to none
        # but it also must point to the next to change
        # it
        prev,cur = None,head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev