"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        m = {}
        # Step 1: create copy of nodes (next pointers)
        oldTemp = head
        newHead = Node(head.val)
        m[head] = newHead
        newTemp = newHead
        oldTemp = head.next
        while oldTemp:
            copyNode = Node(oldTemp.val)
            m[oldTemp] = copyNode
            newTemp.next = copyNode
            newTemp = newTemp.next
            oldTemp = oldTemp.next
        # Step 2: assign random pointers
        oldTemp = head
        newTemp = newHead
        while oldTemp:
            if oldTemp.random:
                newTemp.random = m[oldTemp.random]
            else:
                newTemp.random = None
            oldTemp = oldTemp.next
            newTemp = newTemp.next
        return newHead