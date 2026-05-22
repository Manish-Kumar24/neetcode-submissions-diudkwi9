class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            # already connected -> cycle found
            if rootX == rootY:
                return False

            parent[rootY] = rootX
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]