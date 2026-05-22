class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}

        # build graph
        for (a, b), val in zip(equations, values):

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, target, visited):

            if src not in graph:
                return -1.0

            if src == target:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:

                if nei not in visited:

                    res = dfs(nei, target, visited)

                    if res != -1.0:
                        return weight * res

            return -1.0

        ans = []

        for u, v in queries:
            ans.append(dfs(u, v, set()))

        return ans