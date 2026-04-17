class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.map[idx]):
            if k == key:
                self.map[idx][i] = (key, value)  
                return
        self.map[idx].append((key, value))  
    
    def get(self, key):
        idx = self._hash(key)
        for k, v in self.map[idx]:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.map[idx]):
            if k == key:
                self.map[idx].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)