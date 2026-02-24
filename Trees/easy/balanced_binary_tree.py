# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.right, self.left = 0, 0
        
        def height(node):
            if not node:
                return 0
            
            if abs(self.right - self.left) > 1:
                return False
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            self.right = right_height
            self.left = left_height
            
            return max(left_height, right_height) + 1
        
        height(root)
        return True