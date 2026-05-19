class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        q = deque()
        for node in range(n):
            if degree[node] == 1:
                q.append(node)
        remaining = n
        while remaining > 2:
            size = len(q)
            remaining -= size
            for _ in range(size):
                leaf = q.popleft()
                for nbr in adj[leaf]:
                    degree[nbr] -= 1
                    if degree[nbr] == 1:
                        q.append(nbr)
        return list(q)