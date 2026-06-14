# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) :
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # root = 1
        if not root :
            return 0
        
        diameter = self.maxHeight(root.left) + self.maxHeight(root.right)
        return max(diameter, self.maxDiameter)

    def maxHeight(self, root) :
        if root == None :
            return 0
        
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)

        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
        
        return 1 + max(leftHeight, rightHeight)