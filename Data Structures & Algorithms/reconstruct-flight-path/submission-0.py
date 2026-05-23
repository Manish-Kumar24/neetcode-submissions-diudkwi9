class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        for src in adj:
            adj[src].sort(reverse=True)
        route = []
        def dfs(airport):
            while adj[airport]:
                nxt = adj[airport].pop()
                dfs(nxt)
            route.append(airport)
        dfs("JFK")
        return route[::-1]