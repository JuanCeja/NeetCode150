# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return result

        result = 1
        max = root.val

        return self.dfs(root, max, result)

    def dfs(self, root: TreeNode, max: int, result: int):
        if not root:
            return result

        max = max
        result = result

        if root.val > max:
            max = root.val
            result = 0
            return result

        if root.left:
            if root.left.val < max:
                result += 1
            self.dfs(root.left, max, result)
        if root.right:
            if root.right.val < max:
                result += 1
            self.dfs(root.right, max, result)





        