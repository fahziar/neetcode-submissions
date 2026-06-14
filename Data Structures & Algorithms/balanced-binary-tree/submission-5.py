# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) :
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        
        self.maxDepth(root)
        
        return self.balanced
        
    def maxDepth(self, root) :
        if not root :
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if abs(leftDepth - rightDepth) > 1 :
            self.balanced = False
        
        return 1 + max(leftDepth, rightDepth)
        