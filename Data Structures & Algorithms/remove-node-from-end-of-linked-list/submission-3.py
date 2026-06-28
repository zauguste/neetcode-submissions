# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper_rev(head):
                        curr = head
                        prev = None
                        while curr:
                            hold = curr.next
                            curr.next = prev
                            prev = curr
                            curr = hold
                        return prev


        head = helper_rev(head)

        if n == 1:
            head = head.next
        else:


            curr = head
            # start at head #1
            x = 1
            while curr and curr.next: #n is the num we delete and we want point to n-1 ref to n+1 reference
                if x == n-1: #4
                    curr.next = curr.next.next #3 = 2
                    break
                
                curr = curr.next
                x+=1
        return helper_rev(head)
# n = 2
#     [1,2,3,4]
#     # x = 1
#     # reverse= [4,3,2,1]
#     # while x != n: traverse ll
#        hold_next_node = 3 
#         [4,2,1]
#        cu| |.|.next
#          cu.next = 2








