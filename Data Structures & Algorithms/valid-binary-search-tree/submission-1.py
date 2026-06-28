# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,node, left,right):
      # check 
      if node is None:
          return True
      #   return True
      if not (left < node.val < right):
        return False
      # check the left child against the current node and same with right
      return self.helper(node.left, left, node.val) and self.helper(node.right, node.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      return self.helper(root,float('-inf'),float('inf'))
      
  #           2
  #         /    \
  # .   ..1<2     2<....
  #     / \ 
  #    0   1.5
  #   /
  # none    

      # helper(node, left,right):
      # check if node is None:
      #   return True
      # if not (left < node.val < right):
      #   return False
      # check the left child against the current node and same with right
      # return (node.left, left, node.val) and (node.right, node.val, right)
      # helper(root,float('-inf'),float('inf'))