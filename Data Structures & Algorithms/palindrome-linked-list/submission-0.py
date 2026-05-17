# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head
        def solve(curr):
            if not curr:
                return True
            if not solve(curr.next):
                return False
            if self.front.val != curr.val:
                return False
            self.front = self.front.next
            return True
        return solve(head)