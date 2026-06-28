# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # notes: 
        # we have a binary tree and we are given the root.
        # we want to invert the tree and return its root

        # so to invert is to swap
        # and based on our diagram we have 
        #    1
        #   / \
        # 2     3 ->

        #    1
        #   / \
        # 3     2 
        if not root:
            return
        
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        












        
        # first start at the root
        # check if the head is None:
            # go left
            # go right
            # swap
        # check the head again until none
        if root is None:
            return None
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root