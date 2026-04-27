# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        curr = head
        prev = None
        # Step 1: move to left position
        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        left_prev = prev      # node before left
        tail = curr           # will become tail after reverse
        # Step 2: reverse from left to right
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Step 3: reconnect
        if left_prev:
            left_prev.next = prev
        else:
            head = prev   # case when left = 1
        tail.next = curr
        return head