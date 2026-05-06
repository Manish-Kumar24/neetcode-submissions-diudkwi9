# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0
            cnt = 0
            if node.val >= maxSoFar:
                cnt += 1
            maxSoFar = max(maxSoFar, node.val)
            cnt += dfs(node.left, maxSoFar)
            cnt += dfs(node.right, maxSoFar)
            return cnt
        return dfs(root, root.val)