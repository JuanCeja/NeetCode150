# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = 0
        
        def dfs(node_p, node_q) -> int:
            if not node:
                return 0
            
            if node_p.left.val == node_q.left.val:
                dfs(node_p.left)
                dfs(node_q.left)
                
            if node_p.right.val == node_q.right.val:
                dfs(node_p.right)
                dfs(node_q.right)
                
            
            else:
                return 1
            
        dfs(p)
        dfs(q)
        return is_same == 0