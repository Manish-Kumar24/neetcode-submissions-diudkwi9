# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # push first node of each list
        for row, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, row, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, row, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, row, node.next))
        return dummy.next