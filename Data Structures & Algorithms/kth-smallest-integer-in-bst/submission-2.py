# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # notes
        # we have bst. we want to get the kth smallest in the tree.
        # because this is bst

        #   -2
        #   / \
        # -1   3-
        # / 
        #null
        # k = 2
        # stack = []
        # count = 
        # | |
        #   return 2
        count = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count+=1
            if k == count:
                return curr.val
            curr = curr.right
            

