class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.set = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.set[idx]:
            self.set[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.set[idx]:
            self.set[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.set[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)