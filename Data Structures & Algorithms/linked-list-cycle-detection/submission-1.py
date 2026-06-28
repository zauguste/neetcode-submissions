# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # notes
        # lets say we begin at the head and want to determine if there is a cycle
        # slow fast pointers
        # while fast and fast.next
        #      
                # if f == s:
                #     return True
                #     fs           
        #  none,1 , 2,3,4 -> none
        # false

        #  s      f 
        #       s f 
        # [none,1,2]
        slow,fast = head,head

        while fast and fast.next:
   
            fast = fast.next.next
            slow = slow.next         
            if fast == slow:
                return True

        return False