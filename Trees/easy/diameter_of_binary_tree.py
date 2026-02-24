# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.diameterOfBinaryTree(root.left)
        right_depth = self.diameterOfBinaryTree(root.right)
        
        diameter = (left_depth + right_depth) + 1
        
        return max(left_depth, right_depth) + 1