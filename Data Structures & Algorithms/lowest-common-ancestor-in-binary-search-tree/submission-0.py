# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None, False, False
            left_node, left_p, left_q = dfs(node.left)
            right_node, right_p, right_q = dfs(node.right)
            found_p = left_p or right_p or node.val == p.val
            found_q = left_q or right_q or node.val == q.val
            if left_node:
                return left_node, found_p, found_q
            if right_node:
                return right_node, found_p, found_q
            if found_p and found_q:
                return node, found_p, found_q
            return None, found_p, found_q
        lca, fp, fq = dfs(root)
        return lca if fp and fq else None