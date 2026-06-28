# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(curr) -> Optional[TreeNode]:
        # first lets chech if we are at the end if not
            if curr is None:#1,3,6
                return None
            # swap
            curr.left, curr.right = curr.right,curr.left
            # call helper on the left and right tree
            helper(curr.left)
            helper(curr.right)
            # return the current node
            return curr
        return helper(root)