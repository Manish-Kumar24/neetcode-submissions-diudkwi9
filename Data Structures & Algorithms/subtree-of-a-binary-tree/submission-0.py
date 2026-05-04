# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return (
                isSame(t1.left, t2.left) and
                isSame(t1.right, t2.right)
            )
        if not root:
            return False
        if isSame(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )