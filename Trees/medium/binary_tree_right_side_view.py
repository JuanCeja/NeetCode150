# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            qLen = len(queue)
            
            for _ in range(qLen - 1):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            last_node = queue.popleft()
            
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)
            result.append(last_node.val)
            
        return result
