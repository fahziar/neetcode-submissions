# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        data = self.toList(root)

        return data[k-1]
    
    def toList(self, root) :
        if not root:
            return deque()
        
        mid = deque()
        mid.append(root.val)

        return self.toList(root.left) + mid + self.toList(root.right)
        