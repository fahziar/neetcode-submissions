# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #       1
    #    2      2
    #  3           3    
    # 4 4
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        
        return self.isBalanced(root.right) and self.isBalanced(root.left) and abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
        
    def maxDepth(self, root) :
        if not root :
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        