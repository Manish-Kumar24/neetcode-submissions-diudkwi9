class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = [[] for _ in range(n)]
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node, parent):
            visited.add(node)
            for nbr in adj[node]:
                if nbr not in visited:
                    if not dfs(nbr, node):
                        return False
                elif nbr != parent:
                    return False
            return True
        return dfs(0, -1) and len(visited) == n