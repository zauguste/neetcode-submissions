# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = emptyhead = ListNode()
        head1,head2 = list1,list2
        # [5,6], [2,3,4,10]
        # 2 ->3 -> 4 -> 5 -> 6 -> 10
        # 1. compare the left and right heads and get the smallest to traverse on
        # 2. repeat: add the smaller num to empty list move to next smaller num for that list
        # 3. compare num to left num to right num and take smaller
        # 4. move to next smaller num for that list

        # if null exit and return list
        

        while head1 and head2:
            if head1.val < head2.val:
                emptyhead.next = head1
                head1 = head1.next
            else:
                emptyhead.next = head2 #
                head2 = head2.next  #2,None
            emptyhead = emptyhead.next
    
        emptyhead.next = head1 or head2

        return dummy.next
        # given head of 2 list
        # merge the 2 list into 1
        # return the head of the new list

# Input: list1 = [], list2 = []
# head[null]     head2[null] 
#case 1. if head1 is Null and head2 is Null return []  
# Output: []

# case 2.
# emptyhead = ListNode() -> empty -> 1 -> 2
# Input: list1 = [], list2 = [1,2]
# we want one of these conditions to be true before traversal
# if head1 not Null or head2 not Null:
#    while true:
        # if not head1: []
#           return False
        # emptyhead.next = head1
        # head1 = head1.next


# if head1 not Null or head2 not Null:
#    while true:
        # if not head2: #2,None
#           return False
        # emptyhead.next = head2 #1,2
        # head2 = head2.next  #2,None
# return head.next
 
# Output: [1,2]








