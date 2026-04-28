class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def popLeft(self):
        if self.head.next == self.tail:
            return None
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyMap = {}                  # key → node
        self.freqMap = defaultdict(DLL)   # freq → DLL
        self.minFreq = 0

    def update(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)
        # update minFreq
        if freq == self.minFreq and self.freqMap[freq].head.next == self.freqMap[freq].tail:
            self.minFreq += 1
        node.freq += 1
        self.freqMap[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.update(node)
        else:
            if len(self.keyMap) == self.cap:
                # remove LFU
                lfu_list = self.freqMap[self.minFreq]
                node_to_remove = lfu_list.popLeft()
                del self.keyMap[node_to_remove.key]
            new_node = Node(key, value)
            self.keyMap[key] = new_node
            self.freqMap[1].insert(new_node)
            self.minFreq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)