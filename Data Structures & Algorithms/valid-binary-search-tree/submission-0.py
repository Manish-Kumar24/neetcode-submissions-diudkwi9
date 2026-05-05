# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev, self.ans = None, True
        def ino(root):
            if not root or not self.ans:
                return 
            ino(root.left)
            if self.prev is not None and root.val <= self.prev:
                self.ans = False
            self.prev = root.val
            ino(root.right)
        ino(root)
        return self.ans