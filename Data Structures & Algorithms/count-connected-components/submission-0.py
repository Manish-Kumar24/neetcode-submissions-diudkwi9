class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nbr in adj[node]:
                if nbr not in visited:
                    dfs(nbr)
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components