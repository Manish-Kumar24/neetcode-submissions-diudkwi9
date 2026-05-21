class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        dsu = DSU(n)
        factor_map = {}
        for i, num in enumerate(nums):
            x = num
            d = 2
            factors = set()
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 1
            if x > 1:
                factors.add(x)
            for f in factors:
                if f in factor_map:
                    dsu.union(i, factor_map[f])
                else:
                    factor_map[f] = i
        root = dsu.find(0)
        for i in range(1, n):
            if dsu.find(i) != root:
                return False
        return True