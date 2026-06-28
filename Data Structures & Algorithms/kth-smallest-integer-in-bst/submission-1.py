# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # create a stack
        # create a counter to reach the kth element
        n = 0
        stack = []
        curr = root
        # while there is a node to go to and elements left to traverse
        while curr or stack:
            # while there is a node to go to
            while curr:
#           keep going as left as possible
#           but add to the stack to process
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
            
