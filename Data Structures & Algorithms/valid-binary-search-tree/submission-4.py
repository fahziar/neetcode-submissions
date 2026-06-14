# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = -1001
        maxVal = 1001

        return self.isValid(root, minVal, maxVal)

        
        
    def isValid(self, root, minVal, maxVal) :
        if not root :
            return True
        
        if root.val <= minVal or root.val >= maxVal  :
            return False
        
        return self.isValid(root.left, minVal, root.val) and self.isValid(root.right, root.val, maxVal)
        
        
        