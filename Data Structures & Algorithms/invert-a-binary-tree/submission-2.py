# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
# Input: root = [1,2,3,4,5,6,7]


        
        # notes
    # has all the orders of bst
    # this is a bst
    # using dfs
    # when given the root
    # recursively swap left w right
    # recursively swap right w left
    #  1
    # / \
    # 2 3
     # 1
    # / \
    # 3  2 
    # /\ /\
    # 76 54

    
    # o(n)   
